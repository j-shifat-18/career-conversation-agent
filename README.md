# 🤖 AI Personal Assistant — Md Jahirul Islam Shifat

A conversational AI agent that represents **Md Jahirul Islam Shifat** online. Visitors can chat with the agent to learn about his background, skills, projects, and career — and if they want to connect, the agent captures their details and fires a real-time push notification directly to Shifat's phone.

---

## ✨ Features

- **Conversational AI** — Powered by OpenAI `gpt-4o-mini`, the agent answers questions about Shifat's career, education, skills, and experience in a professional and engaging tone.
- **Rich Personal Context** — The agent is grounded with Shifat's LinkedIn profile, resume (PDF), and a personal summary so answers are accurate and personalized.
- **Lead Capture** — When a visitor expresses interest in connecting, the agent asks for their email and records it along with conversation context.
- **Push Notifications** — Every time someone shares their contact details or asks a question the agent can't answer, Shifat gets an instant push notification via [Pushover](https://pushover.net/).
- **Unknown Question Logging** — Questions the agent can't answer are recorded and sent as notifications so Shifat can improve the agent over time.
- **Clean Chat UI** — Built with [Gradio](https://gradio.app/) for a simple, polished web interface.

---

## 🗂️ Project Structure

```
.
├── main.py                  # Core app — Me class, chat logic, Gradio UI
├── config.py                # Environment config (API keys, model name)
├── requiements.txt          # Python dependencies
├── .env                     # Secret keys (not committed)
│
├── me/
│   ├── summary.txt          # Personal bio and summary
│   ├── j_shifat_resume.pdf  # Resume (parsed at startup)
│   └── linkedin_profile.pdf # LinkedIn profile (parsed at startup)
│
├── tools/
│   ├── tools.py             # OpenAI function/tool definitions (JSON schemas)
│   ├── registry.py          # Maps tool names to Python functions
│   ├── user_tools.py        # record_user_details — saves contact + notifies
│   └── misc_tools.py        # record_unknown_question — logs gaps + notifies
│
└── notification/
    └── notify.py            # Pushover push notification sender
```

---

## ⚙️ How It Works

1. **Startup** — The `Me` class loads Shifat's resume, LinkedIn PDF, and summary text into the system prompt.
2. **Chat** — User messages are sent to GPT-4o-mini with the full personal context. The model responds in character as Shifat.
3. **Tool Calls** — If the model decides to record a user's email or log an unknown question, it calls the appropriate tool:
   - `record_user_details` → saves name, email, and conversation notes, then sends a push notification.
   - `record_unknown_question` → logs the unanswered question and sends a push notification.
4. **Notification** — Both tools trigger a real-time Pushover notification to Shifat's phone.
5. **UI** — Gradio serves the chat interface on `localhost` (or any configured host).

---

## 🚀 Getting Started

### 1. Clone the repo

```bash
git clone <repo-url>
cd <repo-folder>
```

### 2. Create a virtual environment and install dependencies

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
pip install -r requiements.txt
```

### 3. Set up environment variables

Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key
PUSHOVER_USER_KEY=your_pushover_user_key
PUSHOVER_API_TOKEN=your_pushover_app_token
```

- Get your OpenAI key at [platform.openai.com](https://platform.openai.com/)
- Get Pushover credentials at [pushover.net](https://pushover.net/) (free tier available)

### 4. Add your personal files

Place the following in the `me/` folder:
- `j_shifat_resume.pdf` — your resume
- `linkedin_profile.pdf` — your LinkedIn profile export
- `summary.txt` — a short personal bio

### 5. Run the app

```bash
python main.py
```

The Gradio UI will launch and print a local URL (usually `http://127.0.0.1:7860`).

---

## 🔧 Configuration

All configuration lives in `config.py`:

| Variable | Description |
|---|---|
| `MODEL` | OpenAI model to use (default: `gpt-4o-mini`) |
| `OPENAI_API_KEY` | Loaded from `.env` |
| `PUSHOVER_USER_KEY` | Loaded from `.env` |
| `PUSHOVER_API_TOKEN` | Loaded from `.env` |

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| LLM | OpenAI GPT-4o-mini |
| UI | Gradio |
| PDF Parsing | PyPDF2 |
| Push Notifications | Pushover |
| Config Management | python-dotenv |

---

## 👤 About Shifat

**Md Jahirul Islam Shifat** is an aspiring Software Engineer studying at Islamic University of Technology (IUT). He is passionate about AI/Agentic AI, Full-Stack Web Development, and Blockchain.

- 📧 info.jahirulsifat@gmail.com
- 💬 WhatsApp: +880 1612872845

---

## 📄 License

This project is personal and not licensed for redistribution. Feel free to use it as inspiration for your own AI personal assistant.
