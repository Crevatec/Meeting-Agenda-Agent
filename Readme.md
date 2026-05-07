# 🤖 Meeting Agenda Agent

An automated AI collaborator that transforms messy meeting notes or brief objectives into professional, time-boxed meeting agendas.

## 📝 Overview
The **Meeting Agenda Agent** is a Python-based utility designed to solve the "aimless meeting" problem. By providing a simple text description of a meeting's goals, the agent uses LLM reasoning to mathematically distribute time, assign owners, and define clear outcomes.

### Why this is different:
Unlike simple chat prompts, this agent uses **OpenAI Structured Outputs**. This means the AI is physically incapable of returning a broken format; it must strictly adhere to the defined Pydantic schema, making it robust enough for production pipelines.

---

## ✨ Features
*   **Structured Data:** Uses Pydantic models for 100% reliable JSON extraction.
*   **Time-Boxing:** Automatically calculates `time_minutes` for each topic to ensure the total duration is respected.
*   **Dual Output:** 
    *   `agenda.txt`: A clean, human-readable report for distribution.
    *   `agenda.json`: A machine-readable file for calendar or database integration.
*   **Error Handling:** Includes robust validation for API calls and file I/O operations.

---

## 🛠️ Tech Stack
*   **Language:** Python 3.14
*   **AI Engine:** OpenAI GPT-4o-mini
*   **Validation:** Pydantic v2
*   **Interface:** OpenAI Beta Parsing API

---

## 🚀 Getting Started

### 1. Prerequisites
*   Python 3.10 or higher.
*   An OpenAI API Key.

### 2. Installation
Clone the repository and install the required dependencies:
```bash
git clone [https://github.com/YOUR_USERNAME/Meeting-Agenda-Agent.git](https://github.com/YOUR_USERNAME/Meeting-Agenda-Agent.git)
cd Meeting-Agenda-Agent
pip install openai pydantic

### Windows PowerShell  
$env:OPENAI_API_KEY="sk-your-key-here"

Run python agent.py

🛡️ License
This project is licensed under the MIT License.
