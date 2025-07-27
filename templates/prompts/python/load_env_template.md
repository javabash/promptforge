---
title: "Python .env Loader Prompt Template"
tags: [template, python, dotenv, security, promptforge]
author: Philip GeLinas
created: {{date}}
last_modified: {{date}}
category: "python/env"
template_type: "code_analysis"
---

# 🧪 Prompt Template: Loading `.env` in Python

## ❓ Prompt Purpose
Guide the AI to analyze or explain Python code that loads environment variables securely using `dotenv`.

## 🧠 Key Concepts
- Environment variable access
- Security best practices (e.g., don’t hardcode secrets)
- `os.getenv()` vs hardcoding
- `.env` file management

## 📝 Prompt Input Example
```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

print("Hello, World!")
print(f"API Key: {api_key}")
