"""
Exercise 1: Basic API Call
==========================
This is the minimum code needed to call Google Gemini API.

What you'll learn:
- Load API keys securely from environment variables
- Configure and initialize the Gemini model
- Make a simple API call
- Get the response text

This shows the fundamentals - Exercise 2 (chatbot.py) shows production practices.
"""

import os
from dotenv import load_dotenv  # Load .env files into environment
import google.generativeai as genai  # Google's Gemini SDK

# ============================================================================
# STEP 1: Load API Key from Environment (Security Best Practice)
# ============================================================================
# Never hardcode API keys in your code! Always use environment variables.
# The .env file contains: GEMINI_API_KEY=your_actual_key_here
load_dotenv()  # This reads the .env file

api_key = os.getenv('GEMINI_API_KEY')  # Get key from environment

# Validate that the API key exists before proceeding
if not api_key:
    raise ValueError(
        "GEMINI_API_KEY not found in .env file.\n"
        "1. Copy .env.example to .env\n"
        "2. Add your API key from https://aistudio.google.com/"
    )

# ============================================================================
# STEP 2: Configure the Gemini SDK
# ============================================================================
# This authenticates all subsequent API calls
genai.configure(api_key=api_key)

print("Available Models:")
for m in genai.list_models():
    # Only list models that support the generateContent method
    if 'generateContent' in m.supported_generation_methods:
        print(f"- {m.name} (Supports generateContent)")

# ============================================================================
# STEP 3: Initialize the Model
# ============================================================================
# Model options:
# - 'gemini-2.5-flash': Fast, efficient (recommended for learning)
# - 'gemini-2.5-pro': More capable, slower, uses more quota
model = genai.GenerativeModel('gemini-2.5-flash')

# ============================================================================
# STEP 4: Make Your First API Call
# ============================================================================
# This is the simplest possible API call - just a prompt and response
prompt = "Explain what an LLM is in one sentence."
response = model.generate_content(prompt)

# ============================================================================
# STEP 5: Display Results
# ============================================================================
print("\nPrompt:", prompt)
print("\nResponse:", response.text)

# ============================================================================
# That's it! You've successfully called an LLM API.
# 
# Next steps:
# 1. Try different prompts
# 2. Run chatbot.py to see production-ready code with error handling,
#    conversation memory, and more features
# ============================================================================

