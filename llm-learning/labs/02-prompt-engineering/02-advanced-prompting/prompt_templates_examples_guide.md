# Prompt Templates - Complete Guide

A comprehensive reference for all 18 production-ready templates organized by category.

---

## 📚 Quick Reference

| Category | Templates | Best For |
|----------|-----------|----------|
| [Sentiment Analysis](#1-sentiment-analysis) | 3 versions | Analyzing text sentiment |
| [Customer Support](#2-customer-support) | 3 versions | Generating support responses |
| [Content Generation](#3-content-generation) | 3 templates | Creating marketing content |
| [Data Extraction](#4-data-extraction) | 3 templates | Extracting structured data |
| [Code Generation](#5-code-generation) | 2 templates | Generating & reviewing code |
| [Summarization](#6-summarization) | 3 templates | Creating summaries |
| [Classification](#7-classification) | 2 templates | Categorizing text |

**Total: 7 categories, 18 templates**

---

## 1. Sentiment Analysis

Analyze text to determine emotional tone (positive, negative, neutral).

### `sentiment_v1` - Zero-Shot (Basic)

**Pattern:** Zero-Shot (No examples, simple instruction)

**When to use:**
- Quick sentiment checks
- Simple positive/negative/neutral classification
- When you need fast responses

**Input:**
- `text` - Text to analyze

**Output:**
- One word: positive, negative, or neutral

**Example:**
```python
lib = PromptLibrary()
template = lib.get_template("sentiment_v1")
messages = template.format_messages(text="I love this product!")
# Output: "positive"
```

---

### `sentiment_v2` - Few-Shot (Improved)

**Pattern:** Few-Shot (With examples to improve accuracy)

**When to use:**
- Need more consistent results
- Want confidence levels
- Better accuracy than v1

**Input:**
- `text` - Text to analyze

**Output:**
- Sentiment + confidence level (high/medium/low)

**Example:**
```python
template = lib.get_template("sentiment_v2")
messages = template.format_messages(text="The service was okay")
# Output: "neutral (confidence: medium)"
```

**What's different from v1:**
- ✅ Includes few-shot examples in system prompt
- ✅ Returns confidence level
- ✅ More accurate for edge cases

---

### `sentiment_v3` - Production (Recommended) ⭐

**Pattern:** Few-Shot + Structured Output (Production-ready with JSON)

**When to use:**
- **Production systems** (always use this!)
- Need structured, parseable output
- Want confidence scores + reasoning
- Require consistent JSON format

**Input:**
- `text` - Text to analyze

**Output (JSON):**
```json
{
  "sentiment": "positive|negative|neutral",
  "confidence": 0.0-1.0,
  "reasoning": "brief explanation"
}
```

**Example:**
```python
template = lib.get_template("sentiment_v3")
messages = template.format_messages(text="Amazing service!")

# Output:
{
  "sentiment": "positive",
  "confidence": 0.95,
  "reasoning": "Strong positive language ('Amazing')"
}
```

**What's different from v2:**
- ✅ JSON output (easy to parse)
- ✅ Numeric confidence (0.0-1.0)
- ✅ Reasoning included
- ✅ Production-ready validation

---

## 2. Customer Support

Generate helpful customer support responses.

### `support_v1` - Zero-Shot (Basic)

**Pattern:** Zero-Shot (Basic instruction-following)

**When to use:**
- Simple support queries
- Internal tools
- Quick prototyping

**Input:**
- `query` - Customer's question

**Output:**
- Plain text response (max 3 sentences)

**Example:**
```python
template = lib.get_template("support_v1")
messages = template.format_messages(
    query="How do I reset my password?"
)
# Output: "To reset your password, click 'Forgot Password' on the login page..."
```

---

### `support_v2` - Context-Aware

**Pattern:** Zero-Shot + Context (Uses dynamic context variables)

**When to use:**
- Need personalized responses
- Have user tier information
- Want to consider history

**Input:**
- `query` - Customer's question
- `user_tier` - "free" or "premium"
- `previous_issues` - Past issues or "None"

**Output:**
- Personalized response based on context

**Example:**
```python
template = lib.get_template("support_v2")
messages = template.format_messages(
    query="My order is delayed",
    user_tier="premium",
    previous_issues="Late delivery (resolved)"
)
# Output: "I apologize for another delay. As a premium member, I'm prioritizing..."
```

**What's different from v1:**
- ✅ Context-aware (user tier, history)
- ✅ Personalized responses
- ✅ Escalation detection

---

### `support_v3` - Production (Recommended) ⭐

**Pattern:** Zero-Shot + Context + Structured Output (Production-ready)

**When to use:**
- **Production customer support systems**
- Need actionable metadata (action, priority)
- Automated workflows
- Analytics and reporting

**Input:**
- `query` - Customer's question
- `user_tier` - "free" or "premium"
- `previous_issues` - Past issues or "None"

**Output (JSON):**
```json
{
  "response": "helpful answer (max 3 sentences)",
  "action": "resolve|escalate|ticket",
  "priority": "low|medium|high",
  "confidence": 0.0-1.0,
  "next_steps": ["step 1", "step 2"]
}
```

**Example:**
```python
template = lib.get_template("support_v3")
messages = template.format_messages(
    query="Order hasn't arrived yet",
    user_tier="premium",
    previous_issues="None"
)

# Output:
{
  "response": "I understand your concern. Let me track your order...",
  "action": "escalate",
  "priority": "high",
  "confidence": 0.9,
  "next_steps": ["Check tracking", "Contact carrier", "Offer refund if >7 days"]
}
```

**What's different from v2:**
- ✅ Structured JSON output
- ✅ Actionable metadata (action, priority)
- ✅ Next steps for automation
- ✅ Production-ready

---

## 3. Content Generation

Create marketing and communication content.

### `blog_post_v1`

**Pattern:** Zero-Shot with detailed instructions

**When to use:**
- Generate blog content
- SEO-friendly articles
- Content marketing

**Input:**
- `topic` - Blog topic
- `keywords` - SEO keywords (comma-separated)
- `tone` - "professional", "casual", "technical", etc.
- `length` - "short" (300-500), "medium" (800-1200), "long" (1500+)

**Output:**
- Complete blog post with headline, introduction, body paragraphs, call-to-action

**Example:**
```python
template = lib.get_template("blog_post_v1")
messages = template.format_messages(
    topic="Benefits of Python for Data Science",
    keywords="Python, data science, pandas, NumPy",
    tone="professional",
    length="medium"
)
```

---

### `social_media_v1`

**Pattern:** Zero-Shot with platform-specific rules

**When to use:**
- Create social media posts
- Platform-specific content
- Marketing campaigns

**Input:**
- `topic` - Post topic
- `platform` - "Twitter", "LinkedIn", "Instagram"
- `tone` - "professional", "casual", "inspirational"

**Output:**
- Platform-optimized post with hashtags and call-to-action

**Example:**
```python
template = lib.get_template("social_media_v1")
messages = template.format_messages(
    topic="Launching our new AI feature",
    platform="LinkedIn",
    tone="professional"
)
# Respects LinkedIn's 3000 char limit, professional tone
```

---

### `email_subject_v1`

**Pattern:** Zero-Shot with constraints

**When to use:**
- Generate email subject lines
- A/B testing email campaigns
- Marketing automation

**Input:**
- `email_content` - Brief summary of email
- `goal` - "sales", "engagement", "information"

**Output:**
- 5 varied subject lines (under 50 characters each)

**Example:**
```python
template = lib.get_template("email_subject_v1")
messages = template.format_messages(
    email_content="New product launch announcement",
    goal="sales"
)
# Output: 5 subject line options for A/B testing
```

---

## 4. Data Extraction

Extract structured information from unstructured text.

### `extraction_v1`

**Pattern:** Zero-Shot + Structured Output

**When to use:**
- Extract custom fields
- Parse arbitrary text
- Flexible data extraction

**Input:**
- `text` - Text to extract from
- `fields` - Comma-separated field names

**Output (JSON):**
- Extracted fields (uses `null` for missing)

**Example:**
```python
template = lib.get_template("extraction_v1")
messages = template.format_messages(
    text="John Doe, age 35, lives in New York. Email: john@example.com",
    fields="name, age, city, email, phone"
)

# Output:
{
  "name": "John Doe",
  "age": 35,
  "city": "New York",
  "email": "john@example.com",
  "phone": null
}
```

---

### `invoice_parser_v1`

**Pattern:** Zero-Shot + Structured Output with schema

**When to use:**
- Parse invoices/receipts
- Accounting automation
- Expense tracking

**Input:**
- `invoice_text` - Raw invoice text (OCR output, PDF text, etc.)

**Output (JSON):**
```json
{
  "invoice_number": "INV-12345",
  "date": "2024-01-15",
  "total_amount": 1250.50,
  "currency": "USD",
  "items": [
    {"description": "Product A", "quantity": 2, "price": 500.00}
  ],
  "vendor": "ACME Corp",
  "customer": "John Doe"
}
```

**Example:**
```python
template = lib.get_template("invoice_parser_v1")
messages = template.format_messages(
    invoice_text="""
    INVOICE #12345
    Date: 01/15/2024
    From: ACME Corp
    Total: $1,250.50
    """
)
```

---

### `resume_parser_v1`

**Pattern:** Zero-Shot + Structured Output with schema

**When to use:**
- Parse resumes/CVs
- Recruitment automation
- Applicant tracking systems

**Input:**
- `resume_text` - Raw resume text

**Output (JSON):**
```json
{
  "name": "Jane Smith",
  "email": "jane@example.com",
  "phone": "+1-555-0123",
  "skills": ["Python", "Machine Learning", "SQL"],
  "experience_years": 5,
  "education": [
    {"degree": "BS Computer Science", "institution": "MIT", "year": 2018}
  ],
  "current_role": "Senior Data Scientist",
  "summary": "Experienced data scientist with ML expertise"
}
```

**Example:**
```python
template = lib.get_template("resume_parser_v1")
messages = template.format_messages(
    resume_text="""
    Jane Smith
    jane@example.com | +1-555-0123
    
    Senior Data Scientist
    5 years of experience in ML and data analysis
    
    Skills: Python, Machine Learning, SQL, TensorFlow
    """
)
```

---

## 5. Code Generation

Generate and review code.

### `code_function_v1`

**Pattern:** Zero-Shot with detailed requirements

**When to use:**
- Generate functions/methods
- Code scaffolding
- Learning/prototyping

**Input:**
- `description` - What the function should do
- `language` - "Python", "JavaScript", "Java", "Go", etc.

**Output:**
- Production-quality function with docstring, type hints, error handling

**Example:**
```python
template = lib.get_template("code_function_v1")
messages = template.format_messages(
    description="validate email address format",
    language="Python"
)

# Output:
"""
def validate_email(email: str) -> bool:
    '''
    Validate email address format.
    
    Args:
        email: Email address to validate
        
    Returns:
        True if valid, False otherwise
    '''
    import re
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return bool(re.match(pattern, email))
"""
```

---

### `code_review_v1`

**Pattern:** Zero-Shot with structured feedback format

**When to use:**
- Review code before merging
- Learning/mentoring
- Security audits

**Input:**
- `code` - Code to review
- `language` - Programming language

**Output:**
- Structured feedback:
  1. Critical Issues (must fix)
  2. Improvements (should fix)
  3. Suggestions (nice to have)
  4. Positive aspects

**Example:**
```python
template = lib.get_template("code_review_v1")
messages = template.format_messages(
    code="""
    def divide(a, b):
        return a / b
    """,
    language="Python"
)

# Output:
"""
CRITICAL ISSUES:
1. No error handling for division by zero
2. No type hints

IMPROVEMENTS:
1. Add input validation
2. Add docstring

POSITIVE:
- Function is concise and clear
"""
```

---

## 6. Summarization

Create summaries in various formats.

### `summary_short_v1`

**Pattern:** Zero-Shot with length constraint

**When to use:**
- Quick overviews
- Email digests
- Executive summaries

**Input:**
- `text` - Text to summarize

**Output:**
- 2-3 sentence summary

**Example:**
```python
template = lib.get_template("summary_short_v1")
messages = template.format_messages(
    text="[Long article about AI trends...]"
)
# Output: "AI adoption is accelerating across industries. Key trends include..."
```

---

### `summary_bullets_v1`

**Pattern:** Zero-Shot with format specification

**When to use:**
- Meeting notes
- Article highlights
- Key points extraction

**Input:**
- `text` - Text to summarize

**Output:**
- 5-7 bullet points (1 sentence each)

**Example:**
```python
template = lib.get_template("summary_bullets_v1")
messages = template.format_messages(
    text="[Long document...]"
)

# Output:
"""
• Key point 1
• Key point 2
• Key point 3
• Key point 4
• Key point 5
"""
```

---

### `meeting_summary_v1`

**Pattern:** Zero-Shot + Structured Output with schema

**When to use:**
- Meeting notes automation
- Action item tracking
- Team collaboration

**Input:**
- `meeting_text` - Meeting transcript or notes

**Output (JSON):**
```json
{
  "key_decisions": ["Decision 1", "Decision 2"],
  "action_items": [
    {"task": "Update docs", "owner": "John", "deadline": "Friday"}
  ],
  "key_discussion_points": ["Topic 1", "Topic 2"],
  "next_steps": ["Schedule follow-up", "Share notes"]
}
```

**Example:**
```python
template = lib.get_template("meeting_summary_v1")
messages = template.format_messages(
    meeting_text="""
    Team standup 2024-01-15
    - John will update documentation by Friday
    - Decided to use PostgreSQL for new feature
    - Discussed API design options
    """
)
```

---

## 7. Classification

Categorize and analyze text.

### `email_classifier_v1`

**Pattern:** Zero-Shot + Structured Output with rules

**When to use:**
- Email routing/triage
- Support ticket classification
- Inbox automation

**Input:**
- `email_text` - Email content

**Output (JSON):**
```json
{
  "category": "sales|support|billing|general|spam",
  "priority": "low|medium|high|urgent",
  "confidence": 0.0-1.0,
  "suggested_action": "brief action to take"
}
```

**Example:**
```python
template = lib.get_template("email_classifier_v1")
messages = template.format_messages(
    email_text="My payment failed and I can't access my account!"
)

# Output:
{
  "category": "billing",
  "priority": "urgent",
  "confidence": 0.95,
  "suggested_action": "Escalate to billing team immediately"
}
```

---

### `intent_classifier_v1`

**Pattern:** Few-Shot + Structured Output with examples

**When to use:**
- Chatbot intent detection
- User query routing
- Conversational AI

**Input:**
- `text` - User's message

**Output (JSON):**
```json
{
  "primary_intent": "question|request|complaint|feedback|other",
  "sub_intent": "more specific intent",
  "confidence": 0.0-1.0,
  "entities": {"entity_type": "entity_value"},
  "sentiment": "positive|negative|neutral"
}
```

**Example:**
```python
template = lib.get_template("intent_classifier_v1")
messages = template.format_messages(
    text="How do I reset my password?"
)

# Output:
{
  "primary_intent": "question",
  "sub_intent": "account_access",
  "confidence": 0.92,
  "entities": {"action": "reset", "target": "password"},
  "sentiment": "neutral"
}
```

---

## 🎯 Template Selection Guide

### By Use Case

| Need | Recommended Template |
|------|---------------------|
| Analyze customer feedback | `sentiment_v3` |
| Automated customer support | `support_v3` |
| Generate blog content | `blog_post_v1` |
| Create social posts | `social_media_v1` |
| Parse invoices | `invoice_parser_v1` |
| Parse resumes | `resume_parser_v1` |
| Generate code | `code_function_v1` |
| Review code | `code_review_v1` |
| Summarize documents | `summary_short_v1` or `summary_bullets_v1` |
| Extract meeting notes | `meeting_summary_v1` |
| Route emails | `email_classifier_v1` |
| Detect user intent | `intent_classifier_v1` |

### By Pattern Type

| Pattern | Templates | Use When |
|---------|-----------|----------|
| **Zero-Shot** | Most templates | Simple tasks, clear instructions work |
| **Few-Shot** | sentiment_v2, v3, intent_classifier_v1 | Need consistent format, better accuracy |
| **Structured Output** | All v3 versions, parsers, classifiers | Production systems, need JSON |
| **Context-Aware** | support_v2, v3 | Personalized responses, user-specific |

---

## 💡 Best Practices

### 1. Version Progression
- **v1**: Start here for prototyping
- **v2**: Use when v1 isn't accurate enough
- **v3**: Always use in production (structured output)

### 2. Production Checklist
- ✅ Use v3 templates (structured JSON output)
- ✅ Enable output validation (`validate_output=True`)
- ✅ Set appropriate config (`factual` for extraction, `balanced` for generation)
- ✅ Monitor latency and token usage
- ✅ A/B test template versions

### 3. Template Customization
All templates can be modified in `prompt_templates.py`:
```python
# Example: Add your own template
self.templates["custom_v1"] = ChatPromptTemplate.from_messages([
    ("system", "Your system instructions..."),
    ("human", "Your user prompt with {variables}")
])
```

---

## 🔧 Usage Examples

### Basic Usage
```python
from prompt_templates import PromptLibrary

lib = PromptLibrary()

# Get a template
template = lib.get_template("sentiment_v3")

# Format with variables
messages = template.format_messages(text="I love this!")

# Use with LLM (via advanced_prompting.py)
```

### With Production System
```python
from advanced_prompting import AdvancedPromptSystem

system = AdvancedPromptSystem("gemini-2.5-flash")

result = system.generate(
    template_name="sentiment_v3",
    variables={"text": "Great product!"},
    config_name="factual",
    validate_output=True,
    required_output_fields=["sentiment", "confidence"]
)

print(result["parsed_json"])  # {"sentiment": "positive", "confidence": 0.9, ...}
```

### List Templates by Category
```python
lib = PromptLibrary()

# All sentiment templates
sentiment_templates = lib.list_templates("sentiment")
# Returns: ['sentiment_v1', 'sentiment_v2', 'sentiment_v3']

# All templates
all_templates = lib.list_templates()
# Returns: All 18 template names
```

---

## 📚 Additional Resources

- **Main README**: `02-advanced-prompting/README.md` - Architecture and setup
- **Template Source**: `prompt_templates.py` - All template definitions
- **Interactive Demo**: `advanced_prompting.py` - Try templates interactively
- **Main README**: `02-advanced-prompting/README.md` - Architecture and setup

---

**Last Updated:** 2024-01-15  
**Total Templates:** 18 across 7 categories  
**All templates use production best practices** (ChatPromptTemplate with system/user role separation)

