#!/bin/bash

# Lab 02 - Advanced Prompting Setup Script
# Sets up the environment for production prompt engineering

echo "🚀 Setting up Lab 02: Advanced Prompt Engineering"
echo "=================================================="

# Check Python version
echo ""
echo "1️⃣ Checking Python version..."
python_version=$(python3 --version 2>&1 | awk '{print $2}')
echo "   Found Python $python_version"

# Create virtual environment
echo ""
echo "2️⃣ Creating virtual environment..."
if [ -d "venv" ]; then
    echo "   Virtual environment already exists, skipping..."
else
    python3 -m venv venv
    echo "   ✅ Virtual environment created"
fi

# Activate virtual environment
echo ""
echo "3️⃣ Activating virtual environment..."
source venv/bin/activate
echo "   ✅ Virtual environment activated"

# Install dependencies
echo ""
echo "4️⃣ Installing dependencies..."
pip install --upgrade pip > /dev/null 2>&1
echo "   Installing LangChain and provider packages..."
pip install -r requirements.txt
echo "   ✅ Dependencies installed"

# Create .env file from example
echo ""
echo "5️⃣ Setting up environment variables..."
if [ -f ".env" ]; then
    echo "   .env file already exists, skipping..."
else
    cp env.example .env
    echo "   ✅ .env file created from env.example"
    echo ""
    echo "   ⚠️  IMPORTANT: Edit .env and add your API keys!"
    echo "   Minimum: GEMINI_API_KEY (free at https://aistudio.google.com/)"
    echo "   Optional: OPENAI_API_KEY, ANTHROPIC_API_KEY, GROQ_API_KEY"
fi

# Print success message
echo ""
echo "=================================================="
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Get API key from https://aistudio.google.com/ (Gemini - FREE)"
echo "2. Edit .env and add your API key(s)"
echo "3. Run: source venv/bin/activate  (activate venv in this terminal)"
echo "4. Test the system:"
echo "   - python prompt_templates.py              # View all templates"
echo "   - python advanced_prompting.py          # Run with Gemini"
echo "   - python advanced_prompting.py gpt-4    # Run with GPT-4"
echo "   - python advanced_prompting.py ollama/llama3  # Run with local model"
echo "5. Once done, type 'deactivate' to exit the virtual environment"
echo ""
echo "For more information, see README.md"
echo "=================================================="

