
---
title: "Explain Python .env Loading Script"
template_source: "load_env_template.md"
created: {{date}}
tags: [prompt, python, dotenv, explanation]
category: "python/env"
---

# 🧪 Prompt: Explain Python .env Loading

## 👨‍💻 Input Code
```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

print("Hello, World!")
print(f"API Key: {api_key}")


## 📖 Code Explanation

This Python script securely loads an environment variable named `OPENAI_API_KEY` using the `dotenv` module and prints its value to the console. Let's break down what each line does:

1. `import os`: This line imports the built-in Python module `os`, which provides a way of using operating system dependent functionality, like reading or writing to the environment.

2. `from dotenv import load_dotenv`: This line imports the `load_dotenv` function from a third-party package named `dotenv`. 

3. `load_dotenv()`: This function call loads environment variables from a file named `.env` in the same directory as the script. The `.env` file is a simple key-value pair file, where each line is in format "KEY=VALUE". This makes it easy to change these values without modifying your source code.

4. `api_key = os.getenv('OPENAI_API_KEY')`: Here, we are retrieving the value of an environment variable named 'OPENAI_API_KEY' by calling `os.getenv()`. If this environment variable does not exist, it will return None.

5. The last two lines print out "Hello, World!" and the value of our API key to the console.

This method of loading secrets like API keys is secure because environment variables are only available to your application and not exposed in your code or version control system (assuming `.env` is added to `.gitignore`). Thus, even if someone gains access to your source code, they will not be able to see these secret values.

Remember: Always avoid hardcoding sensitive data directly into your scripts! Instead, use something like this setup with dotenv or another secure solution for managing your secret keys and other sensitive data.