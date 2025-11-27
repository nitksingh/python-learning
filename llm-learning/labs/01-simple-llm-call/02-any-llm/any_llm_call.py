"""
Generic Production Chatbot - Multi-Provider Support
Works with: OpenAI, Anthropic, Google Gemini, Groq, Ollama

This uses LangChain, the industry-standard framework for LLM applications.
"""

import os
import sys
from typing import List, Dict, Optional
from datetime import datetime
from dotenv import load_dotenv

# LangChain imports
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from langchain_groq import ChatGroq
from langchain_ollama import ChatOllama
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

# Load environment
load_dotenv()


class GenericChatbot:
    """
    Production-ready chatbot supporting multiple LLM providers
    
    Supported Providers:
    - Google Gemini (gemini-2.5-flash, gemini-2.5-pro)
    - OpenAI (gpt-4, gpt-3.5-turbo)
    - Anthropic Claude (claude-3-5-sonnet, claude-3-haiku)
    - Groq (llama3-8b-8192, mixtral-8x7b)
    - Ollama (llama3, mistral, phi3) - Local
    """
    
    # Supported models and their configurations
    SUPPORTED_MODELS = {
        # Google Gemini
        'gemini-2.5-flash': {
            'provider': 'google',
            'display_name': 'Google Gemini 2.5 Flash',
            'api_key_env': 'GEMINI_API_KEY'
        },
        'gemini-2.5-pro': {
            'provider': 'google',
            'display_name': 'Google Gemini 2.5 Pro',
            'api_key_env': 'GEMINI_API_KEY'
        },
        'gemini-2.0-flash': {
            'provider': 'google',
            'display_name': 'Google Gemini 2.0 Flash',
            'api_key_env': 'GEMINI_API_KEY'
        },
        
        # OpenAI
        'gpt-4': {
            'provider': 'openai',
            'display_name': 'OpenAI GPT-4',
            'api_key_env': 'OPENAI_API_KEY'
        },
        'gpt-3.5-turbo': {
            'provider': 'openai',
            'display_name': 'OpenAI GPT-3.5 Turbo',
            'api_key_env': 'OPENAI_API_KEY'
        },
        'gpt-4o': {
            'provider': 'openai',
            'display_name': 'OpenAI GPT-4o',
            'api_key_env': 'OPENAI_API_KEY'
        },
        
        # Anthropic Claude
        'claude-3-5-sonnet-20241022': {
            'provider': 'anthropic',
            'display_name': 'Claude 3.5 Sonnet',
            'api_key_env': 'ANTHROPIC_API_KEY'
        },
        'claude-3-haiku-20240307': {
            'provider': 'anthropic',
            'display_name': 'Claude 3 Haiku',
            'api_key_env': 'ANTHROPIC_API_KEY'
        },
        
        # Groq (Fast inference)
        'llama3-8b-8192': {
            'provider': 'groq',
            'display_name': 'Llama 3 8B (Groq)',
            'api_key_env': 'GROQ_API_KEY'
        },
        'mixtral-8x7b-32768': {
            'provider': 'groq',
            'display_name': 'Mixtral 8x7B (Groq)',
            'api_key_env': 'GROQ_API_KEY'
        },
        
        # Ollama (Local)
        'ollama/llama3': {
            'provider': 'ollama',
            'display_name': 'Llama 3 (Local)',
            'api_key_env': None  # No API key needed
        },
        'ollama/mistral': {
            'provider': 'ollama',
            'display_name': 'Mistral (Local)',
            'api_key_env': None
        },
        'ollama/phi3': {
            'provider': 'ollama',
            'display_name': 'Phi-3 (Local)',
            'api_key_env': None
        },
    }
    
    def __init__(
        self,
        model_name: str,
        temperature: float = 0.7,
        max_tokens: int = 1000,
        system_prompt: Optional[str] = None
    ):
        """
        Initialize the generic chatbot
        
        Args:
            model_name: Model identifier (e.g., 'gemini-2.5-flash', 'gpt-4')
            temperature: Randomness in responses (0.0-1.0)
            max_tokens: Maximum response length
            system_prompt: Optional system instruction
        """
        self.model_name = model_name
        self.temperature = temperature
        self.max_tokens = max_tokens
        self.system_prompt = system_prompt or "You are a helpful AI assistant."
        self.conversation_history: List[Dict[str, str]] = []
        self.llm = None
        
        # Initialize the model
        self._initialize_model()
    
    def _initialize_model(self):
        """Initialize the LLM based on model name"""
        if self.model_name not in self.SUPPORTED_MODELS:
            available = '\n'.join([f"  - {k}" for k in self.SUPPORTED_MODELS.keys()])
            raise ValueError(
                f"Unsupported model: {self.model_name}\n"
                f"Supported models:\n{available}"
            )
        
        config = self.SUPPORTED_MODELS[self.model_name]
        provider = config['provider']
        
        # Check API key if needed
        if config['api_key_env']:
            api_key = os.getenv(config['api_key_env'])
            if not api_key:
                raise ValueError(
                    f"{config['api_key_env']} not found in environment.\n"
                    f"Add it to your .env file to use {config['display_name']}"
                )
        
        # Initialize based on provider
        try:
            if provider == 'google':
                self.llm = ChatGoogleGenerativeAI(
                    model=self.model_name,
                    temperature=self.temperature,
                    max_tokens=self.max_tokens,
                    google_api_key=os.getenv('GEMINI_API_KEY')
                )
            
            elif provider == 'openai':
                self.llm = ChatOpenAI(
                    model=self.model_name,
                    temperature=self.temperature,
                    max_tokens=self.max_tokens,
                    openai_api_key=os.getenv('OPENAI_API_KEY')
                )
            
            elif provider == 'anthropic':
                self.llm = ChatAnthropic(
                    model=self.model_name,
                    temperature=self.temperature,
                    max_tokens=self.max_tokens,
                    anthropic_api_key=os.getenv('ANTHROPIC_API_KEY')
                )
            
            elif provider == 'groq':
                self.llm = ChatGroq(
                    model=self.model_name,
                    temperature=self.temperature,
                    max_tokens=self.max_tokens,
                    groq_api_key=os.getenv('GROQ_API_KEY')
                )
            
            elif provider == 'ollama':
                # Extract model name (remove 'ollama/' prefix)
                model = self.model_name.replace('ollama/', '')
                self.llm = ChatOllama(
                    model=model,
                    temperature=self.temperature,
                    num_predict=self.max_tokens
                )
            
        except Exception as e:
            raise RuntimeError(f"Failed to initialize {config['display_name']}: {e}")
    
    def generate_response(
        self,
        prompt: str,
        save_history: bool = True,
        use_history: bool = True
    ) -> str:
        """
        Generate a response to the user prompt
        
        Args:
            prompt: User's input message
            save_history: Whether to save to conversation history
            use_history: Whether to use conversation context
            
        Returns:
            Bot's response as string
        """
        # Validate prompt
        if not prompt or not prompt.strip():
            raise ValueError("Prompt cannot be empty")
        
        if len(prompt) > 10000:
            raise ValueError("Prompt too long (max 10,000 characters)")
        
        try:
            # Build message list
            messages = []
            
            # Add system message
            messages.append(SystemMessage(content=self.system_prompt))
            
            # Add conversation history if requested
            if use_history:
                for entry in self.conversation_history:
                    messages.append(HumanMessage(content=entry['user']))
                    messages.append(AIMessage(content=entry['bot']))
            
            # Add current prompt
            messages.append(HumanMessage(content=prompt))
            
            # Generate response
            response = self.llm.invoke(messages)
            response_text = response.content
            
            # Save to history
            if save_history:
                self.conversation_history.append({
                    'timestamp': datetime.now().isoformat(),
                    'user': prompt,
                    'bot': response_text
                })
            
            return response_text
        
        except Exception as e:
            error_msg = str(e)
            
            # Handle common errors
            if "API_KEY" in error_msg or "Invalid" in error_msg:
                raise RuntimeError("Invalid API key. Check your .env file.")
            elif "rate_limit" in error_msg.lower():
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
            f.write(f"Model: {self.model_name}\n")
            f.write(f"System: {self.system_prompt}\n")
            f.write("=" * 60 + "\n\n")
            for entry in self.conversation_history:
                f.write(f"[{entry['timestamp']}]\n")
                f.write(f"User: {entry['user']}\n")
                f.write(f"Bot: {entry['bot']}\n")
                f.write("-" * 60 + "\n")
    
    @classmethod
    def list_supported_models(cls) -> Dict[str, List[str]]:
        """List all supported models grouped by provider"""
        grouped = {}
        for model, config in cls.SUPPORTED_MODELS.items():
            provider = config['provider'].split()[0]
            if provider not in grouped:
                grouped[provider] = []
            grouped[provider].append(model)
        return grouped


def print_welcome():
    """Print welcome message"""
    print("=" * 70)
    print("🤖 Generic Multi-Provider Chatbot (Powered by LangChain)")
    print("=" * 70)
    print("\nCommands:")
    print("  • Type your message to chat")
    print("  • 'quit' or 'exit' - Exit the chatbot")
    print("  • 'help' - Show this help message")
    print("  • 'clear' - Clear conversation history")
    print("  • 'history' - Show conversation history")
    print("  • 'save' - Save conversation to file")
    print("  • 'switch <model>' - Switch to a different model")
    print("  • 'models' - List all supported models")
    print("\n" + "=" * 70)


def print_models():
    """Print supported models"""
    grouped = GenericChatbot.list_supported_models()
    print("\n📋 Supported Models:")
    print("-" * 70)
    for provider, models in grouped.items():
        print(f"\n{provider}:")
        for model in models:
            config = GenericChatbot.SUPPORTED_MODELS[model]
            key_info = f"(Needs {config['api_key_env']})" if config['api_key_env'] else "(Local)"
            print(f"  • {model:<30} {key_info}")
    print("-" * 70)


def main():
    """Main function to run the chatbot"""
    # Get model from command line or use default
    if len(sys.argv) > 1:
        model_name = sys.argv[1]
    else:
        model_name = 'gemini-2.5-flash'  # Default
    
    try:
        # Initialize chatbot
        print(f"🔄 Initializing {model_name}...")
        chatbot = GenericChatbot(model_name=model_name)
        print(f"✅ Ready with {GenericChatbot.SUPPORTED_MODELS[model_name]['display_name']}!\n")
        
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
                
                if command == 'models':
                    print_models()
                    continue
                
                if command.startswith('switch '):
                    new_model = command.replace('switch ', '').strip()
                    try:
                        print(f"🔄 Switching to {new_model}...")
                        chatbot = GenericChatbot(model_name=new_model)
                        config = GenericChatbot.SUPPORTED_MODELS[new_model]
                        print(f"✅ Switched to {config['display_name']}!")
                    except Exception as e:
                        print(f"❌ Failed to switch model: {e}")
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
    print("\n💡 Usage:")
    print("  python chatbot_generic.py                    # Use default (Gemini)")
    print("  python chatbot_generic.py gpt-4              # Use GPT-4")
    print("  python chatbot_generic.py claude-3-5-sonnet-20241022  # Use Claude")
    print("  python chatbot_generic.py ollama/phi3      # Use local ollama")
    print()
    
    main()

