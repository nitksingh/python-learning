# Ollama Local Models Setup

Quick guide to run AI models locally on your machine (100% free, no API needed).

---

## Prerequisites

- macOS, Linux, or Windows
- 8GB+ RAM (4GB for phi3)
- ~3GB disk space per model

---

## Setup Steps

### Terminal 1: Start Ollama Server

```bash
# Install Ollama
brew install ollama

# Start server with optimizations (keep this terminal open)
OLLAMA_FLASH_ATTENTION="1" OLLAMA_KV_CACHE_TYPE="q8_0" ollama serve
```

**What this does:**
- Starts Ollama API server on `http://localhost:11434`
- `OLLAMA_FLASH_ATTENTION="1"` - Faster inference
- `OLLAMA_KV_CACHE_TYPE="q8_0"` - Better memory efficiency

---

### Terminal 2: Download Model & Run Chatbot

```bash
# Download the model (first time only)
ollama pull phi3

# Activate your virtual environment
cd llm-learning/labs/01-simple-chatbot/02-generic-chatbot
source venv/bin/activate

# Run the chatbot
python chatbot_generic.py ollama/phi3
```

**That's it!** 🎉

---

## Available Models

| Model | Size | RAM Needed | Best For |
|-------|------|------------|----------|
| `phi3` | 2.3GB | 4GB | Quick testing (recommended) |
| `llama3` | 4.7GB | 8GB | Better quality responses |
| `mistral` | 4.1GB | 6GB | Balanced performance |

**To try different models:**
```bash
ollama pull llama3
python chatbot_generic.py ollama/llama3
```

---

## Quick Commands

```bash
# List downloaded models
ollama list

# Remove a model
ollama rm phi3

# Stop Ollama server
pkill ollama  # or Ctrl+C in Terminal 1
```

---

## Troubleshooting

### "Connection refused"
→ Make sure `ollama serve` is running in Terminal 1

### "Model not found"
→ Run `ollama pull phi3` first

### Slow responses
→ First request loads model into RAM (10-30 seconds)
→ Subsequent requests are faster

---

## Why Ollama?

- ✅ 100% free
- ✅ Works offline
- ✅ Private (data stays on your machine)
- ✅ No API keys needed
- ✅ Fast after initial load
- ✅ Multiple models available

---

**Ready to try?** Just follow Terminal 1 → Terminal 2 steps above!

