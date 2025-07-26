# promptforge
A structured, version-controlled vault of custom AI prompts designed for LangChain, LLM agents, QA automation, and advanced AI workflows. Built using Obsidian, GitHub, and OpenAI — with tags, templates, and smart organization for fast, reusable prompt engineering.

# 🧠 PromptForge

**PromptForge** is a structured vault for building, organizing, and version-controlling high-impact prompts for AI tools like ChatGPT, LangChain, and agentic LLM workflows. Designed for automation engineers, SDETs, and prompt developers who want to scale up prompt engineering with clarity, consistency, and power.

Built using **Obsidian** for local editing, **ChatGPT** for iteration, and **GitHub** for version control and collaboration.

---

## 🚀 Why Use PromptForge?

Most people treat prompts as throwaway text. But you’re building logic. You need:

- ✅ **Reusable prompts** that improve over time  
- ✅ **Version control** to track changes and fixes  
- ✅ **Tags, templates, and folders** for fast search  
- ✅ **Integrated testing** and logging for quality  
- ✅ **Explainability** — what it does, why it matters

PromptForge gives you a complete system for working like a pro.

---

## 🗂️ Vault Structure

```plaintext
PromptForge/
├── prompts/              # All active prompts (organized by domain)
│   ├── langchain/
│   ├── automation/
│   ├── qa/
│   └── misc/
├── templates/            # Templater scaffolds for new prompts
├── logs/                 # Prompt test results and outputs
├── assets/               # Images, diagrams, reference data
├── system/               # Environment and config files (e.g. .env)
└── README.md             # You're here

# 📌 Prompt: Generate Search Summary via LangChain Agent
🏷️ Tags: #langchain #tool-calling #search #sdet
📄 Use Case: Use an agent to search and return top result

## 💬 Prompt
Write a {sentences}-sentence story about the hometown of {who}.

## 🧠 Notes
- Calls the Serper.dev API via LangChain tool
- Useful for content validation, live data injection, QA bots
- See logs/ for output examples

---

## 🔐 Environment Setup

Create a `.env` file in the `system/` directory with your API keys:

```env
OPENAI_API_KEY=your-key-here
SERPER_API_KEY=optional-search-key

git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/yourusername/promptforge.git
git push -u origin main

---

## ✍️ Author

**Philip GeLinas**  
Prompt Engineer · SDET · AI Automation Builder  
📧 [phil.t.gelinas@gmail.com](mailto:phil.t.gelinas@gmail.com)  
🔗 [GitHub Profile](https://github.com/yourusername) <!-- Replace with your actual GitHub URL -->
