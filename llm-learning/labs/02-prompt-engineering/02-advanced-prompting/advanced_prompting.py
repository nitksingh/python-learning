"""
Advanced Prompt Engineering - Interactive Demo

Demonstrates production-ready prompt engineering techniques:
1. Template system: Multiple template versions (v1, v2, v3)
2. Config presets: Control temperature/max_tokens for different use cases
3. System prompts: Role-based prompts with structured output
4. Input validation: Prevent empty/malicious inputs
5. Output validation: JSON schema validation
6. A/B testing: Test template versions with user assignment
7. Multi-model support: Gemini, GPT-4, Claude, Ollama

Usage:
    python advanced_prompting.py                    # Gemini (default)
    python advanced_prompting.py gpt-4              # GPT-4
    python advanced_prompting.py claude-3-5-sonnet  # Claude
    python advanced_prompting.py ollama/llama3      # Ollama
"""

import os
import sys
import json
from typing import Dict, Any, Optional
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_google_genai import ChatGoogleGenerativeAI

try:
    from langchain_openai import ChatOpenAI
except ImportError:
    ChatOpenAI = None

try:
    from langchain_anthropic import ChatAnthropic
except ImportError:
    ChatAnthropic = None

try:
    from langchain_ollama import ChatOllama
except ImportError:
    ChatOllama = None

from prompt_templates import PromptLibrary

# ============================================================================
# CONFIGURATION PRESETS
# ============================================================================

CONFIGS = {
    "factual": {
        "temperature": 0.0,
        "max_tokens": 500,
        "description": "Deterministic, factual responses"
    },
    "balanced": {
        "temperature": 0.7,
        "max_tokens": 1000,
        "description": "Balanced creativity and consistency"
    },
    "creative": {
        "temperature": 1.0,
        "max_tokens": 1500,
        "description": "Maximum creativity"
    }
}

# ============================================================================
# INPUT VALIDATOR
# ============================================================================

class InputValidator:
    """Validates user inputs"""
    
    @staticmethod
    def validate_variables(variables: Dict[str, Any], required_fields: list) -> Dict[str, Any]:
        """Validate that all required fields are present"""
        # Check all required fields exist
        missing = [f for f in required_fields if f not in variables]
        if missing:
            raise ValueError(f"Missing required fields: {missing}")
        
        # Check no empty values
        empty = [k for k, v in variables.items() if not str(v).strip()]
        if empty:
            raise ValueError(f"Empty values for fields: {empty}")
        
        # Check for prompt injection
        for key, value in variables.items():
            if isinstance(value, str):
                if "ignore previous instructions" in value.lower():
                    raise ValueError(f"Suspicious input detected in '{key}'")
        
        return variables

# ============================================================================
# OUTPUT VALIDATOR
# ============================================================================

class OutputValidator:
    """Validates LLM outputs"""
    
    @staticmethod
    def clean_json_response(response: str) -> str:
        """
        Clean common LLM formatting issues from JSON responses.
        
        LLMs often wrap JSON in markdown code fences or add extra text.
        This method strips those to extract the actual JSON.
        """
        response = response.strip()
        
        # Remove markdown code fences
        if response.startswith("```json"):
            response = response[7:]  # Remove ```json
        elif response.startswith("```"):
            response = response[3:]   # Remove ```
        
        if response.endswith("```"):
            response = response[:-3]  # Remove trailing ```
        
        # Strip any remaining whitespace
        response = response.strip()
        
        return response
    
    @staticmethod
    def validate_json(response: str, required_fields: Optional[list] = None) -> Dict[str, Any]:
        """Validate JSON response and required fields"""
        # Clean markdown formatting first
        cleaned_response = OutputValidator.clean_json_response(response)
        
        try:
            data = json.loads(cleaned_response)
        except json.JSONDecodeError as e:
            raise ValueError(f"Invalid JSON response: {e}")
        
        if required_fields:
            missing = [f for f in required_fields if f not in data]
            if missing:
                raise ValueError(f"Missing required fields in output: {missing}")
        
        return data

# ============================================================================
# PRODUCTION PROMPT SYSTEM
# ============================================================================

class AdvancedPromptSystem:
    """
    Advanced prompt system demonstrating production techniques.
    
    Features:
    - Template-based prompting (load from templates/templates.json)
    - Input/output validation
    - Config presets for different use cases
    - A/B testing framework
    - Multi-model support
    """
    
    def __init__(self, model_name: str = "gemini-2.5-flash"):
        self.model_name = model_name
        self.prompt_library = PromptLibrary()
        self.input_validator = InputValidator()
        self.output_validator = OutputValidator()
        self.llm = self._initialize_llm(model_name)
    
    def _initialize_llm(self, model_name: str):
        """Initialize LLM based on model name"""
        load_dotenv()
        
        if "gpt" in model_name.lower():
            if not ChatOpenAI:
                raise ImportError("Install: pip install langchain-openai")
            return ChatOpenAI(model=model_name, api_key=os.getenv("OPENAI_API_KEY"))
        
        elif "claude" in model_name.lower():
            if not ChatAnthropic:
                raise ImportError("Install: pip install langchain-anthropic")
            return ChatAnthropic(model=model_name, api_key=os.getenv("ANTHROPIC_API_KEY"))
        
        elif "ollama" in model_name.lower():
            if not ChatOllama:
                raise ImportError("Install: pip install langchain-ollama")
            model = model_name.split("/")[1] if "/" in model_name else model_name
            return ChatOllama(model=model)
        
        else:  # Default: Gemini
            api_key = os.getenv("GEMINI_API_KEY")
            if not api_key:
                raise ValueError("GEMINI_API_KEY not found in .env")
            return ChatGoogleGenerativeAI(model=model_name, google_api_key=api_key)
    
    def generate(
        self,
        template_name: str,
        variables: Dict[str, Any],
        config_name: str = "balanced",
        validate_output: bool = False,
        required_output_fields: Optional[list] = None
    ) -> Dict[str, Any]:
        """
        Generate response using template
        
        Args:
            template_name: Name of template (e.g., "sentiment_v3")
            variables: Dict with placeholder values (e.g., {"text": "Great!"})
            config_name: Config preset ("factual", "balanced", "creative")
            validate_output: If True, validate JSON output
            required_output_fields: Required fields in JSON output
        
        Returns:
            Dict with response, metadata, and optional parsed JSON
        """
        # Get template
        template = self.prompt_library.get_template(template_name)
        if not template:
            raise ValueError(f"Template '{template_name}' not found")
        
        # Get required variables for this template
        required_vars = template.input_variables
        
        # Validate input variables
        self.input_validator.validate_variables(variables, required_vars)
        
        # Get config
        config = CONFIGS.get(config_name, CONFIGS["balanced"])
        
        # Format prompt (system + user message)
        messages = template.format_messages(**variables)
        
        # Generate response
        print(f"\n🔄 Generating with {self.model_name} (config: {config_name})...")
        import time
        start = time.time()
        
        # Handle different LLM APIs
        if "gemini" in self.model_name.lower():
            # Gemini: Need to reinitialize with config parameters
            api_key = os.getenv("GEMINI_API_KEY")
            llm_with_config = ChatGoogleGenerativeAI(
                model=self.model_name,
                google_api_key=api_key,
                temperature=config["temperature"],
                max_output_tokens=config["max_tokens"]
            )
            response = llm_with_config.invoke(messages)
        else:
            # OpenAI, Anthropic, Ollama: Pass parameters in invoke()
            response = self.llm.invoke(
                messages,
                temperature=config["temperature"],
                max_tokens=config["max_tokens"]
            )
        
        latency = time.time() - start
        response_text = response.content
        
        # Prepare result
        result = {
            "response": response_text,
            "metadata": {
                "template": template_name,
                "config": config_name,
                "model": self.model_name,
                "latency_ms": int(latency * 1000)
            }
        }
        
        # Validate output if requested
        if validate_output:
            try:
                parsed = self.output_validator.validate_json(
                    response_text,
                    required_output_fields
                )
                result["parsed_json"] = parsed
                result["metadata"]["validation"] = "✅ passed"
            except ValueError as e:
                result["metadata"]["validation"] = f"❌ failed: {e}"
        
        return result
    
    def ab_test(
        self,
        user_id: str,
        base_template: str,
        variables: Dict[str, Any],
        versions: list = ["v2", "v3"],
        config_name: str = "balanced"
    ) -> Dict[str, Any]:
        """
        A/B test between template versions
        
        Args:
            user_id: User identifier for consistent assignment
            base_template: Base template name (e.g., "sentiment")
            variables: Variables for template
            versions: Versions to test (e.g., ["v2", "v3"])
            config_name: Config preset
        
        Returns:
            Dict with response and A/B test info
        """
        # Assign user to version (deterministic based on user_id)
        version_idx = hash(user_id) % len(versions)
        assigned_version = versions[version_idx]
        template_name = f"{base_template}_{assigned_version}"
        
        print(f"\n🧪 A/B Test: User '{user_id}' assigned to {assigned_version}")
        
        # Generate with assigned version
        result = self.generate(
            template_name=template_name,
            variables=variables,
            config_name=config_name,
            validate_output=True
        )
        
        # Add A/B test info
        result["ab_test_info"] = {
            "user_id": user_id,
            "assigned_version": assigned_version,
            "test_group": chr(65 + version_idx)  # A, B, C, etc.
        }
        
        return result

# ============================================================================
# INTERACTIVE MENU
# ============================================================================

def display_menu():
    """Display main menu"""
    print("\n" + "=" * 70)
    print("🚀 Advanced Prompt Engineering - Interactive Demo")
    print("=" * 70)
    print("\nChoose a use case:")
    print("  1. Customer Support")
    print("  2. Sentiment Analysis")
    print("  3. A/B Testing (Demo: Compare sentiment_v2 vs sentiment_v3)")
    print("  4. Exit")
    print()

def get_template_choice(use_case: str, prompt_library: PromptLibrary) -> str:
    """Let user select template version"""
    if use_case == "support":
        print("\nAvailable Customer Support templates:")
        print("  1. support_v1 - Basic support response")
        print("  2. support_v2 - With context and urgency")
        print("  3. support_v3 - Structured JSON output (recommended)")
        choice = input("\nSelect template (1-3) [3]: ").strip() or "3"
        return f"support_v{choice}"
    
    elif use_case == "sentiment":
        print("\nAvailable Sentiment Analysis templates:")
        print("  1. sentiment_v1 - Simple sentiment")
        print("  2. sentiment_v2 - With confidence score")
        print("  3. sentiment_v3 - Structured JSON (recommended)")
        choice = input("\nSelect template (1-3) [3]: ").strip() or "3"
        return f"sentiment_v{choice}"
    
    return "sentiment_v3"

def get_config_choice() -> str:
    """Let user select config preset"""
    print("\nAvailable configs:")
    print("  1. factual    - temperature=0.0 (deterministic)")
    print("  2. balanced   - temperature=0.7 (recommended)")
    print("  3. creative   - temperature=1.0 (varied)")
    choice = input("\nSelect config (1-3) [2]: ").strip() or "2"
    
    config_map = {"1": "factual", "2": "balanced", "3": "creative"}
    return config_map.get(choice, "balanced")

def customer_support_flow(system: AdvancedPromptSystem):
    """Customer support use case"""
    print("\n" + "=" * 70)
    print("📞 Customer Support")
    print("=" * 70)
    
    # Select template
    template_name = get_template_choice("support", system.prompt_library)
    
    # Select config
    config_name = get_config_choice()
    
    # Get user input with defaults (based on template requirements)
    print("\nEnter customer query:")
    query = input("Query [How do I reset my password?]: ").strip() or "How do I reset my password?"
    
    # support_v1 only needs query; v2 and v3 need additional context
    if template_name in ["support_v2", "support_v3"]:
        user_tier = input("User tier (free/premium) [free]: ").strip() or "free"
        previous_issues = input("Previous issues [None]: ").strip() or "None"
        variables = {
            "query": query,
            "user_tier": user_tier,
            "previous_issues": previous_issues
        }
    else:
        # support_v1: only query needed
        variables = {"query": query}
    
    # Only validate JSON for support_v3 (which outputs JSON)
    # Only check for minimal required fields (response, action, priority)
    should_validate = template_name == "support_v3"
    required_fields = ["response", "action", "priority"] if should_validate else None
    
    # Generate
    try:
        result = system.generate(
            template_name=template_name,
            variables=variables,
            config_name=config_name,
            validate_output=should_validate,
            required_output_fields=required_fields
        )
        
        # Display result
        print("\n" + "=" * 70)
        print("✅ RESULT")
        print("=" * 70)
        
        if "parsed_json" in result:
            print(json.dumps(result["parsed_json"], indent=2))
        else:
            print(result["response"])
        
        print("\n📊 Metadata:")
        print(f"  Template: {result['metadata']['template']}")
        print(f"  Config: {result['metadata']['config']}")
        print(f"  Model: {result['metadata']['model']}")
        print(f"  Latency: {result['metadata']['latency_ms']}ms")
        if "validation" in result["metadata"]:
            print(f"  Validation: {result['metadata']['validation']}")
            # If validation failed, show raw response for debugging
            if "failed" in result["metadata"]["validation"] and "parsed_json" not in result:
                print(f"\n🔍 Debug - Raw Response:")
                print(f"  {result['response'][:200]}...")  # First 200 chars
    
    except Exception as e:
        print(f"\n❌ Error: {e}")

def sentiment_analysis_flow(system: AdvancedPromptSystem):
    """Sentiment analysis use case"""
    print("\n" + "=" * 70)
    print("😊 Sentiment Analysis")
    print("=" * 70)
    
    # Select template
    template_name = get_template_choice("sentiment", system.prompt_library)
    
    # Select config
    config_name = get_config_choice()
    
    # Get user input with default
    print("\nEnter text to analyze:")
    text = input("Text [This product is amazing! Best purchase ever.]: ").strip() or "This product is amazing! Best purchase ever."
    
    # Prepare variables
    variables = {"text": text}
    
    # Only validate JSON for sentiment_v2 and sentiment_v3 (which output JSON)
    should_validate = template_name in ["sentiment_v2", "sentiment_v3"]
    required_fields = ["sentiment", "confidence"] if template_name == "sentiment_v2" else ["sentiment", "confidence", "reasoning"] if template_name == "sentiment_v3" else None
    
    # Generate
    try:
        result = system.generate(
            template_name=template_name,
            variables=variables,
            config_name=config_name,
            validate_output=should_validate,
            required_output_fields=required_fields
        )
        
        # Display result
        print("\n" + "=" * 70)
        print("✅ RESULT")
        print("=" * 70)
        
        if "parsed_json" in result:
            print(json.dumps(result["parsed_json"], indent=2))
        else:
            print(result["response"])
        
        print("\n📊 Metadata:")
        print(f"  Template: {result['metadata']['template']}")
        print(f"  Config: {result['metadata']['config']}")
        print(f"  Latency: {result['metadata']['latency_ms']}ms")
    
    except Exception as e:
        print(f"\n❌ Error: {e}")

def ab_testing_flow(system: AdvancedPromptSystem):
    """A/B testing use case"""
    print("\n" + "=" * 70)
    print("🧪 A/B Testing - Template Version Comparison")
    print("=" * 70)
    print("\nℹ️  This demonstrates A/B testing framework for comparing prompt templates.")
    print("    Same user ID always gets the same template version (consistent experience).")
    print("    Different user IDs are split between sentiment_v2 and sentiment_v3.")
    print()
    
    # Get user ID with default
    user_id = input("Enter user ID [user123]: ").strip() or "user123"
    
    # Get text with default
    text = input("Enter text to analyze [The service was okay, nothing special.]: ").strip() or "The service was okay, nothing special."
    
    # Select config
    config_name = get_config_choice()
    
    # Run A/B test
    try:
        result = system.ab_test(
            user_id=user_id,
            base_template="sentiment",
            variables={"text": text},
            versions=["v2", "v3"],
            config_name=config_name
        )
        
        # Display result
        print("\n" + "=" * 70)
        print("✅ RESULT")
        print("=" * 70)
        
        if "parsed_json" in result:
            print(json.dumps(result["parsed_json"], indent=2))
        else:
            print(result["response"])
        
        print("\n🧪 A/B Test Info:")
        print(f"  User ID: {result['ab_test_info']['user_id']}")
        print(f"  Assigned Version: {result['ab_test_info']['assigned_version']}")
        print(f"  Test Group: {result['ab_test_info']['test_group']}")
        
        print("\n📊 Metadata:")
        print(f"  Template: {result['metadata']['template']}")
        print(f"  Latency: {result['metadata']['latency_ms']}ms")
    
    except Exception as e:
        print(f"\n❌ Error: {e}")

# ============================================================================
# MAIN
# ============================================================================

def main():
    # Get model from command line
    model_name = sys.argv[1] if len(sys.argv) > 1 else "gemini-2.5-flash"
    
    # Initialize system
    try:
        system = AdvancedPromptSystem(model_name)
        print(f"\n✅ Initialized with model: {model_name}")
    except Exception as e:
        print(f"\n❌ Failed to initialize: {e}")
        return
    
    # Interactive loop
    while True:
        display_menu()
        choice = input("Select option (1-4): ").strip()
        
        if choice == "1":
            customer_support_flow(system)
        elif choice == "2":
            sentiment_analysis_flow(system)
        elif choice == "3":
            ab_testing_flow(system)
        elif choice == "4":
            print("\n👋 Goodbye!")
            break
        else:
            print("\n❌ Invalid choice. Try again.")
        
        input("\nPress Enter to continue...")

if __name__ == "__main__":
    main()

