---
title: Format AI Test Evaluation Prompt
tags: [langchain, prompt-template, qa, test-eval]
description: >
  Formats an AI prompt that asks the model to evaluate a sample API response and determine if it meets expectations. Useful in LangChain-based test automation or validation flows.
input_variables:
  - response
  - evaluation
---

```python
from langchain_core.prompts import ChatPromptTemplate

# 🧠 Define a chat-style prompt for testing API responses using an LLM
chat_template = ChatPromptTemplate.from_messages([
    ("human", "Given the API response: {response}, does it meet the expected structure and status?"),
    ("ai", "The response evaluation is: {evaluation}")
])

# 🧪 Fill in test input data
messages = chat_template.format_messages(
    response="{{response}}",
    evaluation="{{evaluation}}"
)

# 🖨️ Output the final messages for review or use
for msg in messages:
    print(f"{msg.type.upper()}: {msg.content}")
