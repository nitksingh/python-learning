# 02: Any LLM - Multi-Provider Support

Learn to work with ANY LLM provider using a single codebase (powered by LangChain).

---

## 🆕 What's Different from 01-gemini-llm?

| Concept | 01-gemini-llm | 02-any-llm (this lab) |
|---------|---------------|----------------------|
| **Framework** | Direct Gemini API (manual code) | **LangChain** (industry standard framework) |
| **Providers** | Gemini only | **5 providers** (Gemini, OpenAI, Claude, Groq, Ollama) |
| **Message handling** | Manual string building for history | **Built-in message classes** (SystemMessage, HumanMessage, AIMessage) |
| **Code complexity** | More boilerplate | **Less code** - framework handles details |
| **What you learned** | Direct API calls, manual history | **Framework usage**, multi-provider abstraction |

---

## 📝 What You'll Learn

### **File: `any_llm_call.py`** (Universal LLM Caller)

**Learning Flow:**
1. **LangChain framework** - Industry-standard tool for LLM apps (replaces manual code!)
2. **Built-in message classes** - SystemMessage, HumanMessage, AIMessage (framework handles it)
3. **Multi-provider abstraction** - One code, many models (switch with 1 line!)
4. **Automatic history management** - Framework tracks conversation automatically
5. **Provider routing** - Dynamically switch between providers
6. **Error handling** - Unified error handling across all providers

**Key difference from Lab 01:**
- Lab 01: Manual API calls, manual string building for history
- Lab 02: **LangChain framework** - less boilerplate, cleaner code, multi-provider!
- This is how **production AI apps** are built (using frameworks)!

**Supported Providers:**

| Provider | Models | API Key | Cost |
|----------|--------|---------|------|
| **Google Gemini** | gemini-2.5-flash, gemini-2.5-pro | GEMINI_API_KEY | FREE tier |
| **OpenAI** | gpt-4, gpt-3.5-turbo, gpt-4o-mini | OPENAI_API_KEY | Paid |
| **Anthropic** | claude-3-5-sonnet, claude-3-opus | ANTHROPIC_API_KEY | Paid |
| **Groq** | llama3-70b, mixtral-8x7b | GROQ_API_KEY | FREE tier |
| **Ollama** | phi3, llama3, mistral (local) | None | FREE (local) |

---

## 🎯 Why Multi-Provider?

**Benefits:**
- ✅ **Flexibility** - Try different models easily
- ✅ **Cost optimization** - Use cheap models for simple tasks
- ✅ **Fallback** - If one provider fails, try another
- ✅ **Best model for task** - GPT-4 for complex, Gemini for simple
- ✅ **No vendor lock-in** - Switch providers anytime

**Real-world use:**
```python
# Development: Use free Gemini
python any_llm_call.py gemini-2.5-flash

# Local testing: Use Ollama
python any_llm_call.py ollama/phi3
```

---

## 🚀 How to Run

### **Setup (One-time)**

```bash
# 1. Run setup script
./setup.sh

# 2. Add API keys to .env (at least one)
nano .env
# Minimum: GEMINI_API_KEY=your_key_here
# Optional: OPENAI_API_KEY, ANTHROPIC_API_KEY, GROQ_API_KEY

# 3. Activate environment
source venv/bin/activate

# 4. (Optional) Setup Ollama for local models
# See OLLAMA-SETUP.md for instructions
```

### **Run with Different Providers**

```bash
# Google Gemini (FREE - recommended to start)
python any_llm_call.py gemini-2.5-flash

# OpenAI GPT-4 (requires API key)
python any_llm_call.py gpt-4

# Anthropic Claude (requires API key)
python any_llm_call.py claude-3-5-sonnet-20241022

# Groq (FREE - fast inference)
python any_llm_call.py groq/llama3-70b

# Ollama (FREE - local, no API key needed)
python any_llm_call.py ollama/phi3
```

---

## 📊 Provider Comparison

| Feature | Gemini | OpenAI | Claude | Groq | Ollama |
|---------|--------|--------|--------|------|--------|
| **Cost** | FREE tier | Paid | Paid | FREE tier | FREE (local) |
| **Speed** | Fast | Medium | Medium | Very Fast | Depends |
| **Quality** | Good | Excellent | Excellent | Good | Good |
| **Setup** | Easy | Easy | Easy | Easy | Medium |
| **Internet** | Required | Required | Required | Required | Not required |

---

## 📚 Key Concepts Explained

### **1. Using LangChain Framework (NEW!)**

**⚠️ IMPORTANT:** This lab introduces **LangChain**, the industry-standard framework for LLM apps.

**In `01-gemini-llm`** (manual code):
```python
# Manual API call, manual history building
full_prompt = "\n".join(context_messages) + f"\nUser: {prompt}\nAssistant:"
response = model.generate_content(full_prompt)
# You write ALL the code yourself
```

**In `02-any-llm`** (LangChain framework):
```python
# LangChain handles the details!
from langchain_core.messages import SystemMessage, HumanMessage
from langchain_google_genai import ChatGoogleGenerativeAI

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What's the capital of France?")
]
response = llm.invoke(messages)
# Framework handles API calls, message formatting, error handling!
```

**Why LangChain matters:**
- ✅ **Less boilerplate** - framework handles API calls, formatting, etc.
- ✅ **Multi-provider** - same code works for Gemini, GPT, Claude, etc.
- ✅ **Built-in message classes** - SystemMessage, HumanMessage, AIMessage
- ✅ **Industry standard** - used by most production AI apps
- ✅ **Production-ready** - handles errors, retries, logging automatically

---

### **2. LangChain's Message Classes (Cleaner Than Manual Strings)**

**In `01-gemini-llm`** (manual string building):
```python
# You manually build the conversation string
context_messages = []
for entry in self.conversation_history[-5:]:
    context_messages.append(f"User: {entry['user']}")
    context_messages.append(f"Assistant: {entry['bot']}")

full_prompt = "\n".join(context_messages) + f"\nUser: {prompt}\nAssistant:"
# Messy, error-prone, manual formatting!
```

**In `02-any-llm`** (LangChain message classes):
```python
# LangChain provides clean message classes
messages = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="What's the capital of France?"),
    AIMessage(content="Paris"),  # Previous response
    HumanMessage(content="What's its population?")  # New question
]

response = llm.invoke(messages)
# Clean, structured, framework handles formatting!
```

**The pattern:**
```
SystemMessage → HumanMessage → AIMessage → HumanMessage → AIMessage → ...
(once)          (user)         (bot)       (user)         (bot)
```

**Benefits of message classes:**
- ✅ **Cleaner code** - no manual string concatenation
- ✅ **Type safety** - IDE autocomplete, catch errors early
- ✅ **Consistent** - same pattern across all providers
- ✅ **Framework handles formatting** - you just provide content

**Key insight (from Lab 01):**
- LLMs are **STATELESS** - must send full history each time
- LangChain makes this easier with built-in message classes!

---

### **3. Provider Abstraction (Multi-Provider Support)**

**The problem:**
```python
# Without abstraction (BAD - lots of if/else!)
if provider == 'gemini':
    from google.generativeai import GenerativeModel
    model = GenerativeModel('gemini-2.5-flash')
    response = model.generate_content(prompt)
elif provider == 'openai':
    from openai import OpenAI
    client = OpenAI()
    response = client.chat.completions.create(...)
# ... more if/else for each provider!
```

**With LangChain abstraction (GOOD - unified!):**
```python
# Same interface for ALL providers!
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_openai import ChatOpenAI

# Switch providers by changing ONE line:
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash")
# OR
llm = ChatOpenAI(model="gpt-4")

# Same code works for both!
response = llm.invoke(messages)
```

**Benefits:**
- ✅ Write code once, use with any provider
- ✅ Easy to switch providers (change 1 line)
- ✅ Consistent error handling
- ✅ Production-ready patterns

---

### **4. Model Routing (Dynamic Provider Selection)**

**Simple routing:**
```python
# User specifies model via command line
python any_llm_call.py gemini-2.5-flash  # Use Gemini
python any_llm_call.py gpt-4             # Use OpenAI
python any_llm_call.py ollama/phi3       # Use local Ollama
```

**Advanced routing (production pattern):**
```python
# Route based on task complexity
if task_complexity == "simple":
    model = "gemini-2.5-flash"  # Fast, cheap
elif task_complexity == "complex":
    model = "gpt-4"  # Powerful, expensive
else:
    model = "ollama/phi3"  # Local, free

chatbot = GenericChatbot(model_name=model)
```

---

### **5. Fallback Strategy (Resilience)**

**If one provider fails → try another:**

```python
# Production pattern (not in our code, but good to know)
providers = ["gemini-2.5-flash", "gpt-4", "ollama/phi3"]

for provider in providers:
    try:
        chatbot = GenericChatbot(model_name=provider)
        response = chatbot.generate_response(prompt)
        break  # Success! Stop trying
    except Exception as e:
        print(f"Failed with {provider}, trying next...")
        continue  # Try next provider

# Ensures your app stays online even if one provider is down!
```

**Real-world use cases:**
- OpenAI has an outage → automatically switch to Gemini
- API quota exceeded → fallback to local Ollama
- Network issues → use cached responses or different provider

---

## 🎯 When to Use Which Provider?

**Use Gemini when:**
- Learning/experimenting (FREE tier)
- Simple tasks (classification, translation)
- Cost is a concern

**Use GPT-4 when:**
- Complex reasoning required
- Best quality needed
- Budget allows

**Use Claude when:**
- Long context needed (100K+ tokens)
- Safety/ethics important
- Detailed analysis required

**Use Groq when:**
- Speed is critical
- Using open-source models
- FREE tier available

**Use Ollama when:**
- Privacy is critical (local only)
- No internet available
- Zero API costs needed
- Experimenting with models

---

## 📚 Additional Resources

**Ollama Setup:** See [OLLAMA-SETUP.md](./OLLAMA-SETUP.md) for local model setup

**LangChain Docs:** [https://python.langchain.com/](https://python.langchain.com/)

---

## 🎯 Next Steps

After mastering multi-provider usage:
1. Learn **prompt engineering** (Lab 02-prompt-engineering)
2. Build **production AI agents** (Lab 02-prompt-engineering/03-capstone-project)

---

**Duration:** 20-40 minutes | **Level:** Beginner-Intermediate | **Cost:** FREE (with Gemini/Groq/Ollama)
