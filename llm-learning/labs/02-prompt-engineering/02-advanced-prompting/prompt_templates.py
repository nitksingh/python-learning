"""
Production Prompt Templates Library - JSON-BASED ARCHITECTURE

Best practice: Separate configuration (prompts) from code (logic).

ARCHITECTURE:
  • templates.json: All prompt content (easy to edit, version, A/B test)
  • This file: Template loading and management logic

BENEFITS:
  ✅ No hardcoded strings (clean code)
  ✅ Easy maintenance (edit JSON, not code)
  ✅ Version control friendly (clear diffs)
  ✅ A/B testing ready (swap template files)
  ✅ Hot-reload capable (reload without restart)
  ✅ Non-technical team members can edit prompts

This is a HELPER CLASS used by production_prompting.py and interactive_prompting.py.

Usage:
    from prompt_templates import PromptLibrary
    
    lib = PromptLibrary()  # Loads from templates.json
    template = lib.get_template("sentiment_v3")
    messages = template.format_messages(text="I love this!")
"""

import json
from pathlib import Path
from typing import Dict, List, Optional
from langchain_core.prompts import ChatPromptTemplate


class PromptLibrary:
    """
    HELPER CLASS: Loads and manages production-ready prompt templates from JSON.
    
    All templates follow production best practices:
      • Explicit system/user role separation
      • Format instructions in system role (security)
      • Variable placeholders in user role
    """
    
    def __init__(self, template_file: str = "templates/templates.json"):
        """
        Initialize prompt library by loading templates from JSON.
        
        Args:
            template_file: Path to JSON file (default: templates/templates.json)
        
        Raises:
            FileNotFoundError: If template file doesn't exist
            json.JSONDecodeError: If template file is invalid JSON
            ValueError: If template structure is invalid
        """
        self.templates: Dict[str, ChatPromptTemplate] = {}
        self.template_metadata: Dict[str, Dict] = {}
        
        # Resolve path relative to this file's directory
        self.template_file = Path(__file__).parent / template_file
        
        if not self.template_file.exists():
            raise FileNotFoundError(
                f"Template file not found: {self.template_file}\n"
                f"Expected location: {self.template_file.absolute()}"
            )
        
        self._load_templates()
    
    def _load_templates(self):
        """
        Load all templates from JSON file.
        
        Expected JSON structure:
        {
            "template_name": {
                "pattern": "Zero-Shot|Few-Shot|etc",
                "description": "What this template does",
                "input_variables": ["var1", "var2"],
                "messages": [
                    {
                        "role": "system",
                        "content": "single string OR array of strings"
                    }
                ]
            }
        }
        
        NOTE: content can be:
          • String: "single line"
          • Array: ["line 1", "line 2", "line 3"] (joined with newlines)
        """
        try:
            with open(self.template_file, 'r', encoding='utf-8') as f:
                template_data = json.load(f)
        except json.JSONDecodeError as e:
            raise json.JSONDecodeError(
                f"Invalid JSON in {self.template_file}: {e.msg}",
                e.doc,
                e.pos
            )
        
        # Convert JSON to ChatPromptTemplate objects
        for template_name, config in template_data.items():
            try:
                # Validate structure
                if "messages" not in config:
                    raise ValueError(f"Template '{template_name}' missing 'messages' field")
                
                # Store metadata
                self.template_metadata[template_name] = {
                    "pattern": config.get("pattern", "Unknown"),
                    "description": config.get("description", "No description"),
                    "input_variables": config.get("input_variables", [])
                }
                
                # Build message tuples for ChatPromptTemplate
                messages = []
                for msg in config["messages"]:
                    if "role" not in msg or "content" not in msg:
                        raise ValueError(
                            f"Template '{template_name}' has invalid message: {msg}"
                        )
                    
                    # Support both string and array content
                    content = msg["content"]
                    if isinstance(content, list):
                        # Join array elements with newlines for readability
                        content = "\n".join(content)
                    
                    messages.append((msg["role"], content))
                
                # Create ChatPromptTemplate
                self.templates[template_name] = ChatPromptTemplate.from_messages(messages)
                
            except Exception as e:
                raise ValueError(
                    f"Failed to load template '{template_name}': {str(e)}"
                )
        
        print(f"✅ Loaded {len(self.templates)} templates from {self.template_file.name}")
    
    def reload_templates(self):
        """
        Hot-reload templates from JSON file.
        
        Useful for:
          • Development (edit prompts without restarting)
          • A/B testing (switch template versions on the fly)
          • Production (update prompts without deployment)
        """
        self.templates.clear()
        self.template_metadata.clear()
        self._load_templates()
        print(f"🔄 Reloaded {len(self.templates)} templates")
    
    def get_template(self, name: str) -> ChatPromptTemplate:
        """
        Get a specific template by name.
        
        Args:
            name: Template name (e.g., "sentiment_v3")
        
        Returns:
            ChatPromptTemplate ready for formatting
        
        Raises:
            ValueError: If template not found
        
        Example:
            template = lib.get_template("sentiment_v3")
            messages = template.format_messages(text="Great product!")
        """
        if name not in self.templates:
            available = ", ".join(sorted(self.templates.keys()))
            raise ValueError(
                f"Template '{name}' not found.\n"
                f"Available templates: {available}"
            )
        return self.templates[name]
    
    def get_template_info(self, name: str) -> Dict:
        """
        Get metadata about a template without loading it.
        
        Args:
            name: Template name
        
        Returns:
            Dict with pattern, description, input_variables
        
        Example:
            info = lib.get_template_info("sentiment_v3")
            print(info["description"])  # "Production-ready sentiment..."
            print(info["input_variables"])  # ["text"]
        """
        if name not in self.template_metadata:
            raise ValueError(f"Template '{name}' not found")
        return self.template_metadata[name]
    
    def list_templates(self, category: Optional[str] = None) -> List[str]:
        """
        List all available templates, optionally filtered by category.
        
        Args:
            category: Optional filter (e.g., "sentiment", "support", "code")
                     Matches templates starting with category name
        
        Returns:
            Sorted list of template names
        
        Example:
            all_templates = lib.list_templates()
            sentiment_templates = lib.list_templates("sentiment")
        """
        if category:
            return sorted([
                name for name in self.templates.keys()
                if name.startswith(category.lower())
            ])
        return sorted(self.templates.keys())
    
    def list_categories(self) -> Dict[str, List[str]]:
        """
        Group templates by category (based on name prefix).
        
        Returns:
            Dict mapping category name to list of templates
        
        Example:
            categories = lib.list_categories()
            # {
            #     "sentiment": ["sentiment_v1", "sentiment_v2", "sentiment_v3"],
            #     "support": ["support_v1", "support_v2", "support_v3"],
            #     ...
            # }
        """
        categories = {}
        for name in self.templates.keys():
            # Extract category from template name (e.g., "sentiment_v1" -> "sentiment")
            category = name.split("_")[0] if "_" in name else name
            if category not in categories:
                categories[category] = []
            categories[category].append(name)
        
        return {k: sorted(v) for k, v in sorted(categories.items())}
    
    def get_input_variables(self, name: str) -> List[str]:
        """
        Get required input variables for a template.
        
        Args:
            name: Template name
        
        Returns:
            List of variable names (e.g., ["text", "tone"])
        
        Example:
            vars = lib.get_input_variables("blog_post_v1")
            # ["topic", "keywords", "tone", "length"]
        """
        return self.get_template_info(name)["input_variables"]
    
    def validate_variables(self, name: str, variables: Dict) -> bool:
        """
        Check if all required variables are provided.
        
        Args:
            name: Template name
            variables: Dict of variable values
        
        Returns:
            True if all required variables present, False otherwise
        
        Raises:
            ValueError: With helpful message listing missing variables
        
        Example:
            try:
                lib.validate_variables("sentiment_v3", {"text": "Great!"})
            except ValueError as e:
                print(e)  # Lists missing variables
        """
        required = set(self.get_input_variables(name))
        provided = set(variables.keys())
        missing = required - provided
        
        if missing:
            raise ValueError(
                f"Template '{name}' missing required variables: {', '.join(missing)}\n"
                f"Required: {', '.join(sorted(required))}\n"
                f"Provided: {', '.join(sorted(provided))}"
            )
        
        return True
    
    def export_template(self, name: str, output_file: str):
        """
        Export a single template to a JSON file.
        
        Useful for:
          • Sharing templates
          • Creating template variations
          • Template versioning
        
        Args:
            name: Template name to export
            output_file: Path to save JSON file
        
        Example:
            lib.export_template("sentiment_v3", "sentiment_v3_backup.json")
        """
        if name not in self.templates:
            raise ValueError(f"Template '{name}' not found")
        
        # Load original JSON to preserve structure
        with open(self.template_file, 'r') as f:
            all_templates = json.load(f)
        
        # Export just this template
        template_data = {name: all_templates[name]}
        
        output_path = Path(output_file)
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(template_data, f, indent=2, ensure_ascii=False)
        
        print(f"✅ Exported template '{name}' to {output_path}")
    
    def __repr__(self) -> str:
        """String representation showing loaded templates."""
        return (
            f"PromptLibrary("
            f"templates={len(self.templates)}, "
            f"file={self.template_file.name}"
            f")"
        )


# =============================================================================
# UTILITY FUNCTIONS FOR TEMPLATE MANAGEMENT
# =============================================================================

def list_all_templates(template_file: str = "templates.json"):
    """
    Quick helper to list all templates without creating library instance.
    
    Args:
        template_file: Path to template JSON file
    
    Returns:
        Dict of template names and their descriptions
    
    Example:
        templates = list_all_templates()
        for name, info in templates.items():
            print(f"{name}: {info['description']}")
    """
    lib = PromptLibrary(template_file)
    return {
        name: lib.get_template_info(name)
        for name in lib.list_templates()
    }


def validate_template_file(template_file: str = "templates.json") -> bool:
    """
    Validate template file structure without loading into library.
    
    Args:
        template_file: Path to template JSON file
    
    Returns:
        True if valid, raises exception if invalid
    
    Example:
        try:
            validate_template_file("my_templates.json")
            print("✅ Template file is valid")
        except Exception as e:
            print(f"❌ Invalid template file: {e}")
    """
    try:
        lib = PromptLibrary(template_file)
        print(f"✅ Template file is valid ({len(lib.templates)} templates)")
        return True
    except Exception as e:
        print(f"❌ Template file validation failed: {e}")
        raise


# =============================================================================
# EXAMPLE USAGE
# =============================================================================

if __name__ == "__main__":
    """Demonstrate template library usage."""
    
    print("=" * 70)
    print("PROMPT TEMPLATE LIBRARY - JSON-BASED ARCHITECTURE")
    print("=" * 70)
    print()
    
    # Initialize library (loads from templates.json)
    lib = PromptLibrary()
    print()
    
    # Show all categories
    print("📁 TEMPLATE CATEGORIES:")
    print("-" * 70)
    categories = lib.list_categories()
    for category, templates in categories.items():
        print(f"\n{category.upper()}: {len(templates)} templates")
        for template_name in templates:
            info = lib.get_template_info(template_name)
            print(f"  • {template_name:25} ({info['pattern']})")
            print(f"    {info['description']}")
    
    print()
    print("=" * 70)
    print("EXAMPLE: Using sentiment_v3 template")
    print("=" * 70)
    
    # Get template info
    info = lib.get_template_info("sentiment_v3")
    print(f"\nPattern: {info['pattern']}")
    print(f"Description: {info['description']}")
    print(f"Required variables: {info['input_variables']}")
    
    # Use template
    template = lib.get_template("sentiment_v3")
    messages = template.format_messages(text="This product is amazing!")
    
    print("\nFormatted messages:")
    for msg in messages:
        print(f"\n[{msg.type.upper()}]")
        print(msg.content[:200] + "..." if len(msg.content) > 200 else msg.content)
    
    print()
    print("=" * 70)
    print("✅ Template library ready for production use!")
    print("=" * 70)

