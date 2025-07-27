# scripts/test.py

import os
from dotenv import load_dotenv

# ✅ Load environment variables from a .env file
load_dotenv()

# ✅ Get the OpenAI API key from the environment
api_key = os.getenv("OPENAI_API_KEY")

# ✅ Print confirmation output
print("✅ Test script executed successfully!")
print(f"🔐 Your API key (masked): {api_key[:4]}...***")
