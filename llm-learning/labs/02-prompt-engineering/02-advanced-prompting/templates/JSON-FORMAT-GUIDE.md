# JSON Template Format Guide

## 🎯 Production Lessons from Building This Lab

This guide covers **critical production issues** we discovered while building the advanced prompting system.

---

## 📚 Table of Contents

1. [Multi-Line Format (Arrays vs Strings)](#1-multi-line-format-arrays-vs-strings)
2. [LangChain Curly Brace Escaping](#2-langchain-curly-brace-escaping-critical)
3. [LLM Markdown Output Cleaning](#3-llm-markdown-output-cleaning)
4. [Template Structure Reference](#4-template-structure-reference)
5. [Testing Your Templates](#5-testing-your-templates)

---

## 1. Multi-Line Format (Arrays vs Strings)

### ✅ **RECOMMENDED: Multi-Line Array Format**

**Why Use Arrays?**
- ✅ Easier to read - Each line of prompt on its own line
- ✅ Easier to edit - Add/remove/modify individual lines
- ✅ Better Git diffs - See exactly which lines changed
- ✅ No escape characters - No need for `\n` or `\"`
- ✅ Natural formatting - Looks like actual prompt structure

### **Format Comparison**

#### ❌ **Single-Line String (Hard to Maintain)**

```json
{
  "sentiment_v3": {
    "messages": [
      {
        "role": "system",
        "content": "You are a sentiment analysis expert.\n\nCRITICAL: Respond ONLY with valid JSON..."
      }
    ]
  }
}
```

**Problems:**
- Hard to read (all on one line)
- `\n` everywhere (escape characters)
- Hard to see structure
- Difficult to edit specific parts
- Git diffs show entire line changed

#### ✅ **Multi-Line Array (Production Ready)**

```json
{
  "sentiment_v3": {
    "messages": [
      {
        "role": "system",
        "content": [
          "You are a sentiment analysis expert.",
          "",
          "CRITICAL: Respond ONLY with valid JSON in this exact format:",
          "{{\"sentiment\": \"positive\", \"confidence\": 0.95}}",
          "",
          "IMPORTANT: Output ONLY valid JSON, no other text."
        ]
      }
    ]
  }
}
```

**Benefits:**
- ✅ Easy to read (natural line breaks)
- ✅ No escape characters needed
- ✅ Clear structure
- ✅ Easy to edit specific lines
- ✅ Git diffs show exact line changes

---

## 2. LangChain Curly Brace Escaping (CRITICAL!)

### 🐛 **The Problem**

LangChain's `ChatPromptTemplate` treats `{anything}` as a **variable placeholder**.

If you have JSON examples in your prompt, LangChain will think they're variables!

#### ❌ **WRONG (Causes Error)**

```json
{
  "role": "system",
  "content": [
    "Respond with JSON:",
    "{\"field\": \"value\"}"
  ]
}
```

**Error:**
```
❌ Error: Missing required fields: ['"field"']
```

**Why:** LangChain sees `{field}` and thinks it's a variable like `{query}` or `{text}`.

### ✅ **CORRECT (Escape with Double Braces)**

```json
{
  "role": "system",
  "content": [
    "Respond with JSON:",
    "{{\"field\": \"value\"}}"
  ]
}
```

**How it works:**
- `{{` → Renders as `{` (literal opening brace)
- `}}` → Renders as `}` (literal closing brace)

Same as Python f-strings:
```python
f"Literal brace: {{x}}"  # → "Literal brace: {x}"
```

### 📋 **Complete Example**

#### ❌ **BEFORE (Broken)**

```json
{
  "support_v3": {
    "input_variables": ["query", "user_tier"],
    "messages": [
      {
        "role": "system",
        "content": [
          "Respond with JSON format:",
          "{",
          "    \"response\": \"your answer\",",
          "    \"action\": \"resolve\"",
          "}"
        ]
      }
    ]
  }
}
```

**Result:** LangChain tries to find variables named `response`, `action`, etc.

#### ✅ **AFTER (Fixed)**

```json
{
  "support_v3": {
    "input_variables": ["query", "user_tier"],
    "messages": [
      {
        "role": "system",
        "content": [
          "Respond with JSON format:",
          "{{\"response\": \"your answer\", \"action\": \"resolve\"}}"
        ]
      },
      {
        "role": "user",
        "content": "User tier: {user_tier}\nQuery: {query}"
      }
    ]
  }
}
```

**Notice:**
- JSON example uses `{{...}}` (literal braces)
- Actual variables use `{...}` (placeholders)

### 🎯 **Best Practices for JSON Examples in Prompts**

```json
{
  "role": "system",
  "content": [
    "You are a JSON expert.",
    "",
    "CRITICAL: Respond with ONLY valid JSON in this format:",
    "{{\"field1\": \"value\", \"field2\": 123}}",
    "",
    "Field Rules:",
    "• field1: String description",
    "• field2: Number description",
    "",
    "Remember: Output ONLY the JSON object. Nothing else."
  ]
}
```

**Key Points:**
1. ✅ Use `{{...}}` for literal JSON examples
2. ✅ Show example as **single-line valid JSON**
3. ✅ Explain fields **after** the example
4. ✅ Don't use multi-line JSON format (confuses LLMs)
5. ✅ Remove pipe symbols (`|`) - use explicit values

---

## 3. LLM Markdown Output Cleaning

### 🐛 **The Problem**

Even when you tell LLMs to output ONLY JSON, they often wrap it in markdown:

```
```json
{
  "response": "To obtain an API key..."
}
```
```

This is **NOT valid JSON** and will cause `json.loads()` to fail!

### ✅ **The Solution: Output Cleaning**

The `OutputValidator` in `advanced_prompting.py` automatically strips markdown:

```python
@staticmethod
def clean_json_response(response: str) -> str:
    """
    Clean common LLM formatting issues from JSON responses.
    """
    response = response.strip()
    
    # Remove markdown code fences
    if response.startswith("```json"):
        response = response[7:]  # Remove ```json
    elif response.startswith("```"):
        response = response[3:]   # Remove ```
    
    if response.endswith("```"):
        response = response[:-3]  # Remove trailing ```
    
    response = response.strip()
    return response
```

### 🔄 **Processing Flow**

```
LLM Output:
  ```json
  {"field": "value"}
  ```
       ↓
clean_json_response()
       ↓
  {"field": "value"}
       ↓
json.loads()
       ↓
  ✅ Python dict
```

### 🎯 **Production Best Practice**

**Always clean LLM output before parsing:**

```python
# ❌ DON'T do this
data = json.loads(llm_response)  # Will fail on markdown

# ✅ DO this
cleaned = clean_json_response(llm_response)
data = json.loads(cleaned)  # Works reliably
```

---

## 4. Template Structure Reference

### **Complete Production Template Example**

```json
{
  "sentiment_v3": {
    "pattern": "Few-Shot + Structured Output",
    "description": "Production-ready sentiment analysis with JSON output",
    "input_variables": ["text"],
    "messages": [
      {
        "role": "system",
        "content": [
          "You are a sentiment analysis expert.",
          "",
          "CRITICAL: Respond ONLY with valid JSON in this exact format:",
          "{{\"sentiment\": \"positive\", \"confidence\": 0.95, \"reasoning\": \"brief explanation\"}}",
          "",
          "Field Rules:",
          "• sentiment: Must be exactly one of: positive, negative, neutral",
          "• confidence: Number between 0.0 and 1.0",
          "• reasoning: Brief explanation (max 1 sentence)",
          "",
          "Examples:",
          "• \"Amazing service!\" → {{\"sentiment\": \"positive\", \"confidence\": 0.95, \"reasoning\": \"Strong positive language\"}}",
          "• \"Worst ever\" → {{\"sentiment\": \"negative\", \"confidence\": 0.98, \"reasoning\": \"Extremely negative\"}}",
          "• \"It's fine\" → {{\"sentiment\": \"neutral\", \"confidence\": 0.80, \"reasoning\": \"Neutral, non-committal\"}}",
          "",
          "IMPORTANT: Output ONLY valid JSON, no other text."
        ]
      },
      {
        "role": "user",
        "content": "Analyze this text: {text}"
      }
    ]
  }
}
```

### **Key Elements Explained**

| Element | Purpose | Best Practice |
|---------|---------|---------------|
| `pattern` | Document prompting technique | Use standard names (Zero-Shot, Few-Shot, etc.) |
| `description` | Explain what template does | One clear sentence |
| `input_variables` | List required variables | Match all `{variable}` in content |
| `messages` | System + User prompts | Use arrays for multi-line content |
| `{{...}}` | Literal JSON examples | Always escape curly braces in examples |
| `{variable}` | Actual placeholders | Single braces for real variables |

---

## 5. Testing Your Templates

### **Validate JSON Syntax**

```bash
# Mac/Linux
python3 -m json.tool templates.json

# Windows
python -m json.tool templates.json

# Should output formatted JSON if valid
# Shows error message and line number if invalid
```

### **Test Template Loading**

```python
from prompt_templates import PromptLibrary

# Load templates
lib = PromptLibrary("templates/templates.json")
print(f"✅ Loaded {len(lib.templates)} templates")

# Check a specific template
template = lib.get_template("sentiment_v3")
info = lib.get_template_info("sentiment_v3")

print(f"\nPattern: {info['pattern']}")
print(f"Description: {info['description']}")
print(f"Required variables: {info['input_variables']}")

# Test formatting
messages = template.format_messages(text="This is great!")
print("\nFormatted System Prompt:")
print(messages[0].content)  # Should show properly formatted prompt with {{...}} rendered as {...}
```

### **Expected Output**

```
✅ Loaded 19 templates

Pattern: Few-Shot + Structured Output
Description: Production-ready sentiment analysis with JSON output
Required variables: ['text']

Formatted System Prompt:
You are a sentiment analysis expert.

CRITICAL: Respond ONLY with valid JSON in this exact format:
{"sentiment": "positive", "confidence": 0.95, "reasoning": "brief explanation"}

Field Rules:
• sentiment: Must be exactly one of: positive, negative, neutral
...
```

Notice: `{{...}}` in JSON → `{...}` in rendered prompt ✅

---

## 📋 Common Mistakes to Avoid

### ❌ **DON'T: Use unescaped braces in JSON examples**

```json
"content": [
  "Output format:",
  "{\"field\": \"value\"}"  ← ERROR! LangChain thinks {field} is a variable
]
```

### ✅ **DO: Escape with double braces**

```json
"content": [
  "Output format:",
  "{{\"field\": \"value\"}}"  ← CORRECT! Renders as literal JSON
]
```

### ❌ **DON'T: Show multi-line JSON format to LLMs**

```json
"content": [
  "Output:",
  "{",
  "    \"field\": \"value\"",
  "}"  ← Confuses LLMs - they may output line-by-line
]
```

### ✅ **DO: Show single-line valid JSON**

```json
"content": [
  "Output:",
  "{{\"field\": \"value\"}}"  ← Clear single-line example
]
```

### ❌ **DON'T: Use pseudo-syntax with pipes**

```json
"content": [
  "{{\"status\": \"success|failure\"}}"  ← Ambiguous
]
```

### ✅ **DO: Show actual valid JSON + explain separately**

```json
"content": [
  "{{\"status\": \"success\"}}",
  "",
  "Field Rules:",
  "• status: Must be one of: success, failure"  ← Clear explanation
]
```

### ❌ **DON'T: Mix `\n` in array elements**

```json
"content": [
  "Line 1\nLine 2",  ← Unnecessary and confusing
  "Line 3"
]
```

### ✅ **DO: One line per array element**

```json
"content": [
  "Line 1",
  "Line 2",
  "Line 3"
]
```

---

## 🎓 Production Lessons Summary

### **Three Critical Issues We Fixed:**

1. **LangChain Template Syntax**
   - **Problem**: `{field}` in JSON examples treated as variables
   - **Solution**: Escape with `{{field}}` for literal braces
   - **Impact**: Without this, templates fail to load

2. **LLM Markdown Output**
   - **Problem**: LLMs wrap JSON in ` ```json ... ``` ` despite instructions
   - **Solution**: Always clean/strip markdown before parsing
   - **Impact**: Without this, JSON parsing fails

3. **Multi-Line JSON Format**
   - **Problem**: Showing JSON as multi-line confuses LLMs
   - **Solution**: Show single-line valid JSON + explain fields separately
   - **Impact**: Better LLM compliance with format

### **Best Practices Checklist**

- [ ] Use arrays for multi-line prompts (3+ lines)
- [ ] Escape JSON examples with `{{...}}`
- [ ] Show single-line valid JSON to LLMs
- [ ] Explain fields **after** the JSON example
- [ ] Clean LLM output before parsing
- [ ] Test templates with actual LLM calls
- [ ] Validate JSON syntax with `python -m json.tool`
- [ ] Use meaningful template names and descriptions
- [ ] Document `pattern` and required `input_variables`

---

## 🚀 Quick Reference

### **For JSON-Outputting Templates:**

```json
{
  "template_name": {
    "pattern": "Structured Output",
    "description": "Clear description",
    "input_variables": ["var1", "var2"],
    "messages": [
      {
        "role": "system",
        "content": [
          "You are an expert.",
          "",
          "CRITICAL: Respond ONLY with valid JSON:",
          "{{\"field1\": \"value\", \"field2\": 123}}",
          "",
          "Field Rules:",
          "• field1: Description",
          "• field2: Description",
          "",
          "Remember: Output ONLY JSON, no markdown."
        ]
      },
      {
        "role": "user",
        "content": "Input: {var1}"
      }
    ]
  }
}
```

### **Key Rules:**

1. ✅ `{{...}}` for JSON examples (literal braces)
2. ✅ `{variable}` for actual variables (placeholders)
3. ✅ Single-line JSON format in examples
4. ✅ Field explanations **after** the example
5. ✅ Always emphasize "ONLY JSON, no other text"

---

**Result:** Clean, maintainable, production-ready prompt templates! 🎯

