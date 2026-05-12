# 🤖 Jarvis — AI Voice Assistant

> A full-stack AI-powered voice assistant inspired by Iron Man's J.A.R.V.I.S, built with Python, Flask, and GPT-4o-mini. Supports voice commands, natural language AI responses, and a sleek futuristic web interface.

![Python](https://img.shields.io/badge/Python-3.10+-blue?style=flat-square&logo=python)
![Flask](https://img.shields.io/badge/Flask-2.x-black?style=flat-square&logo=flask)
![OpenAI](https://img.shields.io/badge/GPT--4o--mini-OpenRouter-purple?style=flat-square)
![Deployed](https://img.shields.io/badge/Deployed-Render-green?style=flat-square)
![License](https://img.shields.io/badge/License-MIT-yellow?style=flat-square)

---

## 🌐 Live Demo

🔗 [https://jarvis-python-project.onrender.com/](https://jarvis-python-project.onrender.com/)

---

## 📸 Preview

![Jarvis Screenshot](https://i.imgur.com/placeholder.png)

> *Futuristic HUD-style interface with arc reactor animation, voice waveform, and real-time AI responses.*

---

## ✨ Features

- 🎤 **Voice Activated** — Say a command in the browser using Web Speech API
- 🧠 **AI Powered** — GPT-4o-mini answers any question in one concise sentence
- 🌐 **Web Control** — Open Google, YouTube, Facebook, Instagram by voice
- ⚡ **Real-time Response** — Flask REST API processes commands instantly
- 🕐 **Smart Commands** — Get current time, date, and more
- 💬 **Session Log** — Full conversation history displayed on screen
- 🎨 **Futuristic UI** — Iron Man inspired dark HUD interface with animations
- 📱 **Responsive** — Works on desktop and mobile browsers

---

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript, Web Speech API |
| Backend | Python, Flask, Flask-CORS |
| AI Model | GPT-4o-mini via OpenRouter API |
| Text-to-Speech | Browser SpeechSynthesis API |
| Deployment | Render (backend + frontend) |
| Version Control | Git, GitHub |

---

## 📁 Project Structure

```
jarvis-ai-voice-assistant/
├── app.py                 # Flask backend — API routes and AI logic
├── requirements.txt       # Python dependencies
├── Procfile               # Render deployment config
├── templates/
│   └── index.html         # Frontend — UI and voice interaction
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites

- Python 3.10+
- OpenRouter API key → [openrouter.ai/keys](https://openrouter.ai/keys)
- Google Chrome (for voice input)

### Local Setup

**1. Clone the repository**
```bash
git clone https://github.com/YOUR_USERNAME/jarvis-ai-voice-assistant.git
cd jarvis-ai-voice-assistant
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Set your API key**

Create a `.env` file in the root folder:
```
OPENROUTER_API_KEY=sk-or-v1-your-key-here
```

Or set it directly in `app.py` for local testing:
```python
api_key=os.environ.get("OPENROUTER_API_KEY", "sk-or-v1-your-key-here")
```

**4. Run the app**
```bash
python app.py
```

**5. Open in Chrome**
```
http://localhost:8080
```

---

## 🗣️ Voice Commands

| Command | Action |
|---|---|
| `Open Google` | Opens google.com |
| `Open YouTube` | Opens youtube.com |
| `Open Facebook` | Opens facebook.com |
| `Open Instagram` | Opens instagram.com |
| `What time is it` | Speaks current time |
| `What is today's date` | Speaks current date |
| `Tell me a joke` | AI responds with a joke |
| `Any question...` | GPT-4o-mini answers in one line |

---

## 🧩 How It Works

```
User speaks or types a command
        ↓
Browser sends POST request to Flask /command
        ↓
Flask checks built-in commands (open, time, date)
        ↓
If no match → sends to GPT-4o-mini via OpenRouter
        ↓
Response returned to browser
        ↓
Browser speaks response using SpeechSynthesis API
```

---

## 🔮 Future Improvements

- [ ] Add Spotify music control
- [ ] Add weather API integration
- [ ] Add reminder and alarm feature
- [ ] Add conversation memory (multi-turn chat)
- [ ] Add custom wake word detection
- [ ] Mobile app version with React Native

---

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the project
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📄 License

This project is licensed under the MIT License — see the [LICENSE](LICENSE) file for details.

---

## 👨‍💻 Author

**Smit** — Cloud Infrastructure & Full Stack Developer

[![GitHub](https://img.shields.io/badge/GitHub-Follow-black?style=flat-square&logo=github)](https://github.com/YOUR_USERNAME)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?style=flat-square&logo=linkedin)](https://linkedin.com/in/YOUR_USERNAME)

---

## ⭐ Show Your Support

If you found this project helpful, please give it a **star** ⭐ on GitHub!

---

*Built with ❤️ and Python*
