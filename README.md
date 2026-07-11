<img width="1024" height="1536" alt="22BCEAC3-0C92-46BC-BDC2-60980095FC08" src="https://github.com/user-attachments/assets/10d2793f-6191-49b1-9381-8a1461e8bc0b" />



# 🤖 Nawanshu's Digital Twin

An AI-powered Digital Twin that represents my professional profile through an interactive conversational interface. Built using Python, Gradio, and Groq LLM, this project enables visitors to learn about my background, technical skills, projects, certifications, and career journey by chatting with an AI assistant trained on my professional information.



## 📌 Overview

The Digital Twin acts as a virtual representation of me, capable of answering career-related questions naturally while maintaining context from my LinkedIn profile and professional summary. It also demonstrates LLM tool calling by recording visitor contact information and logging unanswered questions for future improvement.



## ✨ Features

- 🤖 AI-powered Digital Twin
- 💬 Natural conversational interface
- 📄 LinkedIn profile as knowledge source
- 🧠 Context-aware responses
- 🛠️ Function Calling support
- 📧 Visitor email collection
- ❓ Unknown question logging
- 🎨 Modern Gradio user interface
- ⚡ Powered by Groq Llama 3.3 70B



## 🏗️ System Architecture

```
                Visitor
                   │
                   ▼
          Gradio Web Interface
                   │
                   ▼
         Digital Twin Application
                   │
        ┌──────────┴──────────┐
        ▼                     ▼
  Context Loader        Tool Functions
        │                     │
        ▼                     ▼
Professional Profile     Email Logger
LinkedIn PDF             Question Logger
Summary                  Notifications
        │
        ▼
      Groq LLM
        │
        ▼
 AI Response to Visitor
```



## 🛠️ Technology Stack

| Category | Technologies |
|----------|--------------|
| Programming Language | Python |
| LLM | Groq (Llama 3.3 70B) |
| AI SDK | OpenAI Python SDK |
| UI Framework | Gradio |
| Document Processing | PyPDF |
| Environment Management | Python Dotenv |
| HTTP Requests | Requests |



## 📁 Project Structure

```
Nawanshu-Digital-Twin/
│
├── app.py                # Main Gradio application
├── context.py            # Loads profile data & builds system prompt
├── tools.py              # Function calling implementation
├── styles.py             # UI styling
├── linkedin.pdf          # LinkedIn profile
├── summary.txt           # Professional summary
├── requirements.txt
└── README.md
```



## 🚀 Installation

Clone the repository

```bash
git clone https://github.com/nawanshu18/Nawanshu-Digital-Twin.git
cd Nawanshu-Digital-Twin
```

Create a virtual environment

```bash
python -m venv .venv
```

Activate it

### macOS / Linux

```bash
source .venv/bin/activate
```

### Windows

```bash
.venv\Scripts\activate
```

Install dependencies

```bash
pip install -r requirements.txt
```



## 🔑 Environment Variables

Create a `.env` file in the project root.

```env
GROQ_API_KEY=your_api_key

PUSHOVER_USER=your_user_key

PUSHOVER_TOKEN=your_token
```



## ▶️ Run the Application

```bash
python app.py
```

or

```bash
uv run app.py
```

The application will be available at:

```
http://127.0.0.1:7860
```


## 📷 Screenshots
<img width="1664" height="1256" alt="1B266240-8EBC-4CB3-B7B7-D2E87C1506CA" src="https://github.com/user-attachments/assets/dc84cf5a-e195-4545-8651-edc4cdc16bc2" />



<img width="1664" height="1252" alt="C5A5C143-8A73-4188-93A8-F8259425DAAE" src="https://github.com/user-attachments/assets/d714cb70-4d53-4086-9bad-a2461f6ae9fd" />



<img width="1614" height="1234" alt="D76F25CC-9814-4402-B267-A10CDF04B6BA" src="https://github.com/user-attachments/assets/251b5fc7-107a-467e-8c4c-723e23462105" />



<img width="1632" height="1224" alt="5D2AFCFD-423B-4BB1-AC25-DF76A231E737" src="https://github.com/user-attachments/assets/48123da4-5390-4529-9bd1-7d86e038e187" />




## 💡 Example Questions

- Tell me about yourself.
- What are your strongest technical skills?
- Which AI projects have you built?
- What technologies do you work with?
- How can I contact you?

---

## 🎯 Future Enhancements

- Voice interaction
- Multi-model support
- Public deployment
- Conversation memory
- Portfolio integration
- Resume download
- Analytics dashboard



## 👨‍💻 About Me

I'm **Nawanshu Lahane**, a Computer Science & Engineering student with an interest in Artificial Intelligence, Machine Learning, Agentic AI, Data Science, and Software Development.

This project demonstrates how Large Language Models and function calling can be combined to build an intelligent, interactive digital representation of a professional profile.


## 📫 Connect With Me

**LinkedIn:** https://www.linkedin.com/in/nawanshulahane
**GitHub:** https://github.com/nawanshu18

---

## ⭐ Support

If you found this project interesting, consider giving it a ⭐ on GitHub.

Feedback and contributions are always welcome.
