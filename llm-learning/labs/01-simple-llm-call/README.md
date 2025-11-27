# Lab 01: Simple LLM Call

Learn how to make your first API calls to LLMs (Large Language Models).

---

## 🎯 What You'll Learn

- How to configure and call LLM APIs
- Parameters (temperature, max_tokens)
- Conversation history management
- Working with different LLM providers
- LangChain framework

---

## 📚 Sub-Labs

### **01: Gemini LLM** (Google's Gemini API)

Learn to call Google's Gemini API (free tier available).

**Files:**
- `01_simple_gemini_call.py` - Basic API call
    **Learning Flow:**
    1. Configure SDK with API key
    2. List available models
    3. Select a model
    4. Call the model with a prompt (message)
    5. Print the response
- `02_advanced_gemini_call.py` - Production-ready code
    **Learning Flow:**
    1. Structured code with classes
    2. Input validation (check empty/long inputs)
    3. Error handling (API errors, network issues)
    4. Parameters:
        - `temperature` - Controls randomness (0.0 = consistent, 1.0 = creative)
        - `max_tokens` - Limits response length (prevents long responses)
    5. `save_history` - **THE PROBLEM IT SOLVES:**

👉 **[Start with Gemini](./01-gemini-llm/README.md)**

---

### **02: Any LLM** (Multi-Provider Support)

Learn to work with multiple LLM providers using LangChain.

**Supports:**
- Google Gemini
- OpenAI (GPT-4, GPT-3.5)
- Anthropic (Claude)
- Ollama (local models)

**Files:**
- `any_llm_call.py` - Universal LLM caller

👉 **[Use Any LLM](./02-any-llm/README.md)**

---

## 🚀 Quick Start

```bash
# Option 1: Start with Gemini (recommended for beginners)
cd 01-gemini-llm
./setup.sh
source venv/bin/activate
python 01_simple_gemini_call.py

# Option 2: Use any LLM provider
cd 02-any-llm
./setup.sh
source venv/bin/activate
python any_llm_call.py gemini-2.5-flash
```

---

## 📖 Learning Path

1. **Start:** [01-gemini-llm](./01-gemini-llm/README.md) - Learn basics with Gemini
2. **Next:** [02-any-llm](./02-any-llm/README.md) - Work with multiple providers

---

**Duration:** 30 minutes - 1 hour | **Level:** Beginner | **Cost:** FREE (Gemini)
