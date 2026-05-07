# 🤖 Meeting Agenda Agent

> A Python-based AI agent that transforms a brief meeting description into a professional, time-boxed agenda — complete with owners, outcomes, and structured output ready for calendars or pipelines.
---

## 📝 Overview

The **Meeting Agenda Agent** tackles the "aimless meeting" problem head-on. You provide a plain-text description of your meeting's goals; the agent uses LLM reasoning to distribute time intelligently, assign topic owners, and define clear outcomes for every agenda item.

What makes it production-ready: the agent uses **OpenAI Structured Outputs** with a strict Pydantic schema, meaning the AI is physically constrained to return well-formed JSON every time — no parsing hacks, no brittle string extraction.
---
## ✨ Features

- **Schema-enforced output** — Pydantic v2 models guarantee 100% reliable JSON extraction via OpenAI's Structured Outputs API
- **Automatic time-boxing** — calculates `time_minutes` per topic so the total always matches your target duration
- **Owner & outcome assignment** — each agenda item gets a responsible party and a defined expected outcome
- **Dual output formats:**
  - `agenda.txt` — clean, human-readable report ready to paste into an invite or email
  - `agenda.json` — machine-readable file for calendar, database, or downstream pipeline integration
- **Robust error handling** — graceful validation for API calls and file I/O operations

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Language | Python 3.10+ |
| AI Engine | OpenAI GPT-4o-mini |
| Validation | Pydantic v2 |
| API Interface | OpenAI Beta Parsing API |

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10 or higher
- An [OpenAI API key](https://platform.openai.com/api-keys)

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/Crevatec/Meeting-Agenda-Agent.git
cd Meeting-Agenda-Agent
```

**2. Install dependencies**

```bash
pip install openai pydantic
```

**3. Set your OpenAI API key**

macOS / Linux:
```bash
export OPENAI_API_KEY="sk-your-key-here"
```

Windows (PowerShell):
```powershell
$env:OPENAI_API_KEY="sk-your-key-here"
```

**4. Run the agent**

```bash
python agent.py
```

---

## 📤 Output

After running, two files are generated in the project root:

| File | Format | Purpose |
|---|---|---|
| `agenda.txt` | Plain text | Human-readable — share in emails or meeting invites |
| `agenda.json` | JSON | Machine-readable — integrate with calendars or databases |

---

## 🗂️ Project Structure

```
Meeting-Agenda-Agent/
├── agent.py        # Main agent script
├── agenda.txt      # Generated plain-text agenda
├── agenda.json     # Generated JSON agenda
└── README.md
```
---
## 📄 License

MIT — free to use, modify, and distribute.
