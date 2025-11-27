#!/bin/bash

# Lab 02 - Basic Prompting Setup Script
# Sets up the environment for prompt engineering exercises

echo "🚀 Setting up Lab 02: Basic Prompt Engineering"
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
    echo "   ⚠️  IMPORTANT: Edit .env and add your Gemini API key!"
    echo "   Get your free API key from: https://aistudio.google.com/"
fi

# Print success message
echo ""
echo "=================================================="
echo "✅ Setup complete!"
echo ""
echo "Next steps:"
echo "1. Get your API key from https://aistudio.google.com/"
echo "2. Edit .env and add your API key"
echo "3. Run: source venv/bin/activate  (activate venv in this terminal)"
echo "4. Read README.md (complete prompt engineering guide)"
echo "5. Run: python prompt_lab.py (interactive experimentation)"
echo "6. Modify prompts in prompt_lab.py and re-run"
echo "7. Once done, type 'deactivate' to exit the virtual environment"
echo ""
echo "For more information, see README.md"
echo "=================================================="

