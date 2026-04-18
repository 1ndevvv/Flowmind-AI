# FlowMind AI — Prompt-Based Workflow Assistant
 
<div align="center">
![FlowMind AI](https://img.shields.io/badge/FlowMind-AI-7c6af7?style=for-the-badge&logo=sparkles)
![React](https://img.shields.io/badge/React-18-61dafb?style=for-the-badge&logo=react)
![Gemini](https://img.shields.io/badge/Gemini-2.5_Flash-4285f4?style=for-the-badge&logo=google)
![Status](https://img.shields.io/badge/Status-Live-34d399?style=for-the-badge)
 
**A production GenAI assistant with 7 specialized prompt-based agents — built entirely in a single HTML file.**
 
[🚀 Live Demo](https://1ndevvv.github.io/Flowmind-AI/) · [📂 Source Code](https://github.com/1ndevvv/Flowmind-AI)
 
</div>
---
 
## What is FlowMind AI?
 
FlowMind AI is a **prompt-based workflow assistant** that transforms Google's Gemini LLM into 7 domain-specific AI agents — each with a dedicated system prompt, color theme, and quick-start suggestions.
 
Instead of a generic chat interface, each agent is pre-configured as an expert in its domain — this is the core pattern behind modern production AI agent systems.
 
---
 
## 7 Specialized Agents
 
| Agent | Purpose | Color |
|-------|---------|-------|
| 💬 **Free Chat** | General AI assistant — ask anything | Purple |
| ✉️ **Email Generator** | Professional emails with subject line + tips | Blue |
| 📄 **Text Summarizer** | TL;DR + Key Points + Actionable Takeaway | Green |
| 🗓️ **Action Planner** | Goals → timelines, milestones, daily tasks | Orange |
| 💻 **Code Explainer** | Explain, debug, and improve any code | Pink |
| 🔗 **LinkedIn / Captions** | 3 post variations + hashtags per topic | Yellow |
| 🔍 **Quick Answer** | One-line factual answers, fast | Violet |
 
---
 
## Architecture
 
```
┌─────────────────────────────────────────────┐
│              FlowMind AI Frontend            │
│         React 18 (CDN) + Babel Standalone    │
├─────────────────────────────────────────────┤
│                                             │
│  ┌──────────┐    ┌──────────────────────┐   │
│  │ Sidebar  │    │   Chat Interface     │   │
│  │ 7 Agents │───▶│  Messages + Input    │   │
│  └──────────┘    └──────────┬───────────┘   │
│                             │               │
│              System Prompt Routing          │
│                             │               │
└─────────────────────────────┼───────────────┘
                              │
                    Gemini API Call
                              │
              ┌───────────────▼──────────────┐
              │   Google Gemini 2.5 Flash     │
              │   (generativelanguage API)    │
              └──────────────────────────────┘
```
 
### Key Design Patterns
 
**Prompt Routing Architecture** — Each agent passes a unique `system_instruction` to Gemini, transforming the same LLM into a domain-specific expert:
 
```javascript
const WORKFLOWS = [
  {
    id: 'email',
    systemPrompt: `You are an expert email writer. When given a brief description,
    generate a professional, clear, and well-structured email with subject line,
    greeting, body, and sign-off...`
  },
  // ... 6 more agents
]
```
 
**Multi-Turn Conversation State** — Chat history maintained per agent using React state:
 
```javascript
const callGemini = async (messages, systemPrompt) => {
  const contents = messages.map(m => ({
    role: m.role === 'assistant' ? 'model' : 'user',
    parts: [{ text: m.content }]
  }));
  // Full history sent each API call for context
};
```
 
**Per-Agent Chat Isolation** — Each agent has its own independent conversation history stored in a single `chats` state object keyed by workflow ID.
 
---
 
## Tech Stack
 
| Layer | Technology |
|-------|-----------|
| Frontend | React 18 (CDN), Babel Standalone |
| AI Model | Google Gemini 2.5 Flash |
| Hosting | GitHub Pages |
| Fonts | Syne, DM Sans, DM Mono |
| Auth | API key stored in localStorage |
 
> **No build step. No npm install. No backend.** The entire app ships as a single `index.html`.
 
---
 
## Features
 
- **7 specialized AI agents** with unique system prompts
- **Per-agent chat history** — switch between agents without losing context
- **Quick prompt chips** — pre-built suggestions for each workflow
- **Copy to clipboard** — one-click copy for any AI response
- **Clear chat** — reset individual agent conversations
- **Responsive** — sidebar collapses to horizontal scroll on mobile
- **API key persistence** — stored in localStorage, no re-entry needed
---
 
## Getting Started
 
### 1. Get a Free Gemini API Key
Visit [Google AI Studio](https://aistudio.google.com/app/apikey) and create a free API key.
 
### 2. Open the App
Go to **[https://1ndevvv.github.io/Flowmind-AI/](https://1ndevvv.github.io/Flowmind-AI/)**
 
### 3. Enter Your Key
Paste your Gemini API key in the modal and click **Connect & Launch**.
 
### 4. Start Using Agents
Select any agent from the sidebar and start chatting!
 
---
 
## Run Locally
 
No installation needed. Just clone and open:
 
```bash
git clone https://github.com/1ndevvv/Flowmind-AI.git
cd Flowmind-AI
# Open index.html in your browser
open index.html
```
 
---
 
## What It Can Do
 
✅ Multi-turn conversations with full context  
✅ 7 specialized domains with expert system prompts  
✅ Persistent API key across sessions  
✅ Independent chat history per agent  
✅ Quick prompt suggestions per workflow  
✅ Copy responses to clipboard  
✅ Mobile responsive layout  
 
## What It Cannot Do
 
❌ No file upload or document reading  
❌ No image generation or vision capabilities  
❌ No real-time web search (Gemini knowledge cutoff applies)  
❌ No user accounts or cloud sync  
❌ No streaming responses (waits for full reply)  
❌ API key in localStorage — not secure for production multi-user deployment  
 
---
 
## Limitations & Future Improvements
 
| Current | Improvement |
|---------|------------|
| localStorage API key | Backend proxy to hide key |
| No streaming | Server-Sent Events for real-time typing |
| Single HTML file | Proper Vite + React build pipeline |
| No persistence | Database for conversation history |
| CDN React | Production bundle with tree-shaking |
 
---
 
## Project Structure
 
```
Flowmind-AI/
└── index.html          ← Entire application (React + CSS + JS)
```
 
The entire app — React components, styles, and logic — lives in a single `index.html`. This was an intentional architectural choice for zero-friction GitHub Pages deployment.
 
---
 
## Interview Talking Points
 
**Q: Why a single HTML file?**  
Zero build process, instant GitHub Pages deployment. Tradeoff: not scalable for production but perfect for a portfolio project.
 
**Q: How does the agent routing work?**  
Each workflow has a `systemPrompt` string injected as `system_instruction` in the Gemini API call. Same LLM, different persona and output format — core prompt engineering pattern.
 
**Q: How is conversation history managed?**  
React `useState` with a `chats` object keyed by workflow ID. Each API call sends the full message history so Gemini maintains context across turns.
 
**Q: What would you do differently in production?**  
Move API calls to a FastAPI backend, add streaming, implement user auth, use Vite for bundling, and store conversations in a database.
 
---
 
## About the Developer
 
**Devanshu Shah** — AI & Full-Stack Developer  
BCA Graduate, Amity University (2022–2025)
 
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0077b5?style=flat&logo=linkedin)](https://linkedin.com/in/devanshu-shah-b6a316262)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-333?style=flat&logo=github)](https://github.com/1ndevvv)
[![Portfolio](https://img.shields.io/badge/Portfolio-FlowMind_AI-7c6af7?style=flat)](https://1ndevvv.github.io/Flowmind-AI/)
 
---
 
<div align="center">
  <sub>Built with React 18 + Google Gemini API · Deployed on GitHub Pages</sub>
</div>
