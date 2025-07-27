---
title: LangChain ChatPromptTemplate
tags: [langchain, prompts, qa]
description: Format structured chat messages with variable injection
---

## 🧠 Purpose

Use LangChain's `ChatPromptTemplate` to build testable, structured AI message flows.
Perfect for simulating question/answer exchanges in QA automation or AI agents.

---

## 💻 Code Template

```python
from langchain_core.prompts import ChatPromptTemplate

# 🧠 Define a chat prompt for an AI test agent validating an API response
chat_template = ChatPromptTemplate.from_messages([
    ("human", "Given the API response: {response}, does it meet the expected structure and status?"),
    ("ai", "The response evaluation is: {evaluation}")
])

# 🧪 Fill in test data
messages = chat_template.format_messages(
    response='{"status":"ok","data":{"id":123,"value":"active"}}',
    evaluation="✅ Status is OK and required fields are present."
)

# 📤 Output formatted messages
for msg in messages:
    print(f"{msg.type.upper()}: {msg.content}")

