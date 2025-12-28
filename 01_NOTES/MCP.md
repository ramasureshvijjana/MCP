## 🔹 What is MCP?
**MCP (Model Context Protocol)** is a **standard way for an AI model to talk to external tools and data** (files, APIs, databases).

👉 Think of MCP as a **universal connector for AI**.

---

## 🔹 What is the use of MCP?
MCP helps an AI to:
- 📂 Read files  
- 🗄️ Query databases  
- 🌐 Call APIs  
- 🔍 Fetch data for RAG  
- 🤖 Use tools safely  

**Without MCP:** every tool needs custom code  
**With MCP:** plug once, use everywhere  

---

## 🔹 How MCP works (Simple Flow)

User Question  
↓  
LLM  
↓  
MCP  
↓  
Tools (DB / API / Files)  
↓  
MCP  
↓  
LLM  
↓  
Answer  

---

**One-line Example :**
> “Get farming expenses from DB”

LLM → MCP → Database → MCP → LLM → Answer ✅

---

## 🔹 Real-life Analogy
- **LLM** = Brain 🧠  
- **MCP** = Remote control 🎮  
- **Tools** = TV, AC, Lights  

One remote → control everything.

---

## 🔹 In short
> **MCP lets AI safely use external tools in a standard and easy way.**
