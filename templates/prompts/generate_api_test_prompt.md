---
name: generate_api_test_prompt
description: Generate a Python test case based on API endpoint behavior
tags: [langchain, qa, testgen]
---

HUMAN: Write a Python test using pytest that validates the following API behavior:
- Endpoint: {{endpoint}}
- Method: {{method}}
- Expected Status Code: {{status}}
- Expected Keys in Response: {{keys}}
- Sample Payload: {{payload}}

AI: Sure! Here's a test case that matches the criteria:
