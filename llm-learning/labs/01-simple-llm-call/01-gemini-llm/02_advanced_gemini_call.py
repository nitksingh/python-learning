"""
Production-Ready Chatbot with Google Gemini
Best practices for LLM applications
"""

import os
import sys
import time
from typing import Optional, List, Dict
from datetime import datetime
from dotenv import load_dotenv
import google.generativeai as genai
from google.generativeai.types import GenerationConfig

# Load environment
load_dotenv()

class GeminiChatbot:
    """Production-ready chatbot using Google Gemini"""
    
    def __init__(
        self,
        model_name: str = 'gemini-2.5-flash',
        temperature: float = 0.7,
        max_tokens: int = 1000,
    ):
        """
        Initialize the chatbot
        
        Args:
            model_name: Gemini model to use
            temperature: Randomness in responses (0.0-1.0)
            max_tokens: Maximum response length
        """
        self.model_name = model_name
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.conversation_history: List[Dict[str, str]] = []
        self.model = None
        
        # Initialize
        self._validate_environment()
        self._initialize_model()
    
    def _validate_environment(self):
        """Validate environment setup"""
        api_key = os.getenv('GEMINI_API_KEY')
        if not api_key:
            raise ValueError(
                "GEMINI_API_KEY not found in environment. "
                "Please create a .env file with your API key."
            )
        genai.configure(api_key=api_key)
    
    def _initialize_model(self):
        """Initialize the Gemini model"""
        try:
            self.model = genai.GenerativeModel(
                model_name=self.model_name,
                generation_config=GenerationConfig(
                    temperature=self.temperature,
                    max_output_tokens=self.max_tokens,
                )
            )
        except Exception as e:
            raise RuntimeError(f"Failed to initialize model: {e}")
    
    def generate_response(
        self,
        prompt: str,
        save_history: bool = True
    ) -> str:
        """
        Generate a response to the user prompt
        
        IMPORTANT: If save_history=True, this method:
        1. Retrieves previous conversation from self.conversation_history
        2. Builds a FULL prompt including previous exchanges
        3. Sends this full context to the model (so model "remembers")
        4. Saves the new exchange back to history for the next call
        
        Example with history:
            Call 1: "Capital of France?" → Saves to history
            Call 2: Sends to model: "User: Capital of France?\nAssistant: Paris\nUser: Population?"
                    (Model sees "Paris" in the prompt, so it remembers!)
        
        Args:
            prompt: User's input message
            save_history: Whether to save to conversation history and include
                         previous exchanges in the prompt sent to the model
            
        Returns:
            Bot's response as string
            
        Raises:
            ValueError: If prompt is invalid
            RuntimeError: If API call fails
        """
        # Validate prompt
        if not prompt or not prompt.strip():
            raise ValueError("Prompt cannot be empty")
        
        if len(prompt) > 10000:
            raise ValueError("Prompt too long (max 10,000 characters)")
        
        try:
            # Build context from conversation history (if save_history is enabled)
            # This is the KEY: we send previous conversation to the model!
            if save_history and self.conversation_history:
                # Format: Include last few exchanges for context
                context_messages = []
                for entry in self.conversation_history[-5:]:  # Last 5 exchanges
                    context_messages.append(f"User: {entry['user']}")
                    context_messages.append(f"Assistant: {entry['bot']}")
                
                # Combine history + current prompt
                full_prompt = "\n".join(context_messages) + f"\nUser: {prompt}\nAssistant:"
            else:
                # No history - just send current prompt
                full_prompt = prompt
            
            # Generate response with context
            response = self.model.generate_content(full_prompt)
            
            # Extract response text
            response_text = response.text if response.text else ""
            
            # Check for blocked content
            if not response_text:
                response_text = (
                    "⚠️ Response was blocked due to safety filters. "
                    "Please try rephrasing your question."
                )
            
            # Save to history (for next call)
            if save_history:
                self.conversation_history.append({
                    'timestamp': datetime.now().isoformat(),
                    'user': prompt,
                    'bot': response_text
                })
            
            return response_text
        
        except Exception as e:
            error_msg = str(e)
            
            # Handle specific errors
            if "API_KEY_INVALID" in error_msg:
                raise RuntimeError("Invalid API key")
            elif "RESOURCE_EXHAUSTED" in error_msg:
                raise RuntimeError("Rate limit exceeded. Please wait and try again.")
            elif "quota" in error_msg.lower():
                raise RuntimeError("API quota exceeded")
            else:
                raise RuntimeError(f"API error: {error_msg}")
    
    def get_history(self) -> List[Dict[str, str]]:
        """Get conversation history"""
        return self.conversation_history.copy()
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history = []
    
    def save_history_to_file(self, filename: str):
        """Save conversation history to file"""
        with open(filename, 'w') as f:
            for entry in self.conversation_history:
                f.write(f"[{entry['timestamp']}]\n")
                f.write(f"User: {entry['user']}\n")
                f.write(f"Bot: {entry['bot']}\n")
                f.write("-" * 60 + "\n")

def print_welcome():
    """Print welcome message"""
    print("=" * 60)
    print("🤖 Welcome to Gemini Chatbot!")
    print("=" * 60)
    print("\nCommands:")
    print("  • Type your message to chat")
    print("  • 'quit' or 'exit' - Exit the chatbot")
    print("  • 'help' - Show this help message")
    print("  • 'clear' - Clear conversation history")
    print("  • 'history' - Show conversation history")
    print("  • 'save' - Save conversation to file")
    print("\n" + "=" * 60)

def main():
    """Main function to run the chatbot"""
    try:
        # Initialize chatbot
        print("🔄 Initializing chatbot...")
        chatbot = GeminiChatbot()
        print("✅ Ready!\n")
        
        # Print welcome
        print_welcome()
        
        # Main chat loop
        while True:
            try:
                # Get user input
                user_input = input("\n💬 You: ").strip()
                
                # Handle empty input
                if not user_input:
                    continue
                
                # Handle commands
                command = user_input.lower()
                
                if command in ['quit', 'exit', 'bye']:
                    print("\n👋 Thank you for chatting! Goodbye!")
                    break
                
                if command == 'help':
                    print_welcome()
                    continue
                
                if command == 'clear':
                    chatbot.clear_history()
                    print("✅ Conversation history cleared!")
                    continue
                
                if command == 'history':
                    history = chatbot.get_history()
                    if not history:
                        print("No conversation history yet.")
                    else:
                        print("\n📜 Conversation History:")
                        print("-" * 60)
                        for entry in history:
                            print(f"[{entry['timestamp']}]")
                            print(f"You: {entry['user']}")
                            print(f"Bot: {entry['bot'][:100]}...")
                            print()
                    continue
                
                if command == 'save':
                    filename = f"chat_history_{datetime.now().strftime('%Y%m%d_%H%M%S')}.txt"
                    chatbot.save_history_to_file(filename)
                    print(f"✅ Conversation saved to {filename}")
                    continue
                
                # Generate response
                response = chatbot.generate_response(user_input)
                print(f"\n🤖 Bot: {response}")
            
            except ValueError as e:
                print(f"❌ Invalid input: {e}")
            
            except RuntimeError as e:
                print(f"❌ Error: {e}")
            
            except KeyboardInterrupt:
                print("\n\n👋 Interrupted. Goodbye!")
                break
    
    except Exception as e:
        print(f"❌ Fatal error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()

