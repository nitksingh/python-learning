# 01: Gemini LLM - Google's Gemini API

Learn to call Google's Gemini API (free tier available).

---

## 📝 What You'll Learn

### **File 1: `01_simple_gemini_call.py`** (Basic API Call)

**Learning Flow:**
1. Configure SDK with API key
2. List available models
3. Select a model
4. Call the model with a prompt (message)
5. Print the response

**💡 Key Concepts for Lab 1:**

#### **What is a Prompt?**

A **prompt** is the text/instruction you send to an LLM to get a response.

**Example:**
```python
prompt = "What's the capital of France?"
response = model.generate_content(prompt)
```

#### **Message Roles (3 Types)**

Production AI apps use **3 message roles** for better control:

| Role | Purpose | Example |
|------|---------|---------|
| **system** | Developer's instructions, rules, behavior | "You are a helpful math tutor." |
| **user** | End user's question/input | "What is 25 × 4?" |
| **assistant** | AI's previous responses (for history) | "25 × 4 = 100. Here's how..." |

**Why roles matter:**
- ✅ **Security** - Prevent prompt injection attacks
- ✅ **History** - Multi-turn conversation management
- ✅ **Structure** - Clean separation of instructions vs. data

**📚 Want to learn more about prompting?**

👉 **See [Lab 02: Prompt Engineering → 01-basic-prompting](../../02-prompt-engineering/01-basic-prompting/README.md)** for:
- Detailed role explanations with examples
- Security patterns (prompt injection defense)
- Core prompting patterns (zero-shot, few-shot, chain-of-thought)
- Parameters guide (temperature, top_p, etc.)
- Production best practices

---

### **File 2: `02_advanced_gemini_call.py`** (Production-Ready Code)

**Learning Flow:**
1. Structured code with classes
2. Input validation (check empty/long inputs)
3. Error handling (API errors, network issues)
4. Parameters:
   - `temperature` - Controls randomness (0.0 = consistent, 1.0 = creative)
   - `max_tokens` - Limits response length (prevents long responses)
5. `save_history` - **THE PROBLEM IT SOLVES:**

   **⚠️ CRITICAL CONCEPT: LLMs are STATELESS!**
   
   LLMs (like Gemini, GPT-4, Claude) have **NO MEMORY** between API calls.
   Each call is completely independent - the model doesn't "remember" anything.
   
   **Visual Flow (How History is Actually Sent):**
   ```
   ┌─────────────────────────────────────────────────────────┐
   │  WITHOUT save_history (Each call is independent)        │
   ├─────────────────────────────────────────────────────────┤
   │  Call 1: Send to model: "Capital of France?"           │
   │          Model replies: "Paris"                         │
   │                                                         │
   │  Call 2: Send to model: "What's its population?"       │
   │          Model replies: "Population of what?" ❌        │
   │          (Model never saw previous question!)           │
   └─────────────────────────────────────────────────────────┘
   
   ┌─────────────────────────────────────────────────────────┐
   │  WITH save_history (Context sent back each time)        │
   ├─────────────────────────────────────────────────────────┤
   │  Call 1: Send to model: "Capital of France?"           │
   │          Model replies: "Paris"                         │
   │          ↓ Save to conversation_history[]              │
   │          conversation_history = [                       │
   │            {user: "Capital of France?", bot: "Paris"}   │
   │          ]                                              │
   │                                                         │
   │  Call 2: Build prompt from history + new question:     │
   │          ┌──────────────────────────────────────┐      │
   │          │ User: Capital of France?             │      │
   │          │ Assistant: Paris                     │      │
   │          │ User: What's its population?         │      │
   │          └──────────────────────────────────────┘      │
   │          Send this FULL context to model               │
   │          Model replies: "Paris has 2.1M people" ✅     │
   │          (Model sees the word "Paris" in history!)     │
   └─────────────────────────────────────────────────────────┘
   ```
   
   **The Key Mechanism (in code):**
   ```python
   # Step 1: User asks first question
   response1 = generate_response("Capital of France?", save_history=True)
   # Internally saves: {user: "Capital...", bot: "Paris"}
   
   # Step 2: User asks follow-up
   # Code builds FULL prompt including history:
   full_prompt = """
   User: Capital of France?
   Assistant: Paris
   User: What's its population?
   """
   # THIS full_prompt is sent to model, so it sees "Paris"!
   response2 = generate_response("What's its population?", save_history=True)
   ```
   
   **When to use:** Chatbots, Q&A apps, anything needing context

6. `save_history_to_file` - **THE PROBLEM IT SOLVES:**

   **❌ WITHOUT saving to file:**
   ```
   User reports: "Bot gave wrong answer!"
   You: "What did you ask?" 
   User: "I don't remember exactly..." 
   You: ❌ Can't debug or reproduce the issue
   ```
   
   **✅ WITH saving to file:**
   ```
   User reports: "Bot gave wrong answer!"
   You: Open conversation_123.txt
   You: ✅ See exact conversation, find the bug!
   ```
   
   **Real-world uses:**
   - **Debug:** See what went wrong in production
   - **Audit:** Legal/compliance requirements (who said what when)
   - **Training:** Improve prompts by reviewing real conversations
   - **Share:** Send conversation logs to teammates
   
   **Visual Example:**
   ```
   User Chat → save_history_to_file() → conversation_2024-11-23.txt
   
   File contents:
   ┌────────────────────────────────────────────────┐
   │ [2024-11-23 10:30:15] User: Capital of France?│
   │ [2024-11-23 10:30:16] Bot: Paris              │
   │ [2024-11-23 10:31:20] User: Population?       │
   │ [2024-11-23 10:31:21] Bot: 2.1M people        │
   └────────────────────────────────────────────────┘
   ```
   
   **When to use:** Production apps, customer support, legal/compliance

**💡 Additional Key Concepts for Lab 2:**

#### **Parameters (Brief)**

- **`temperature`** (0.0 - 1.0): Controls randomness
  - `0.0` = Consistent, deterministic responses
  - `0.7` = Balanced (default)
  - `1.0` = Creative, varied responses

- **`max_tokens`**: Limits response length
  - Prevents overly long responses
  - Controls costs (charged per token)

---

## 🚀 How to Run

### **Setup (One-time)**

```bash
# 1. Run setup script
./setup.sh

# 2. Add your API key to .env
nano .env
# Add: GEMINI_API_KEY=your_key_here
# Get free key from: https://aistudio.google.com/

# 3. Activate environment
source venv/bin/activate
```

### **Run Programs**

```bash
# Basic call (start here!)
python 01_simple_gemini_call.py

# Advanced call (production-ready)
python 02_advanced_gemini_call.py
```

---

## ✅ What You've Learned

**From Lab 1 (`01_simple_gemini_call.py`):**
- ✅ What a prompt is and how to send it
- ✅ 3 message roles (system, user, assistant) and why they matter
- ✅ How to authenticate and make basic API calls

**From Lab 2 (`02_advanced_gemini_call.py`):**
- ✅ **CRITICAL:** LLMs are STATELESS (no memory between calls!)
- ✅ How to "fake" memory using `save_history`
- ✅ Why persist conversations with `save_history_to_file`
- ✅ Production patterns (validation, error handling, parameters)

---

## 🎯 Next Steps

After mastering these:
1. Try `02-any-llm` to work with multiple LLM providers
2. Explore `02-prompt-engineering` for advanced techniques

---

**Duration:** 15-30 minutes | **Level:** Beginner | **Cost:** FREE
