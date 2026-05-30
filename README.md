# 🎯 AI Career Advisor Chatbot

🔗 **Live Demo:**
https://careeradvisorchatbot-drqxrcyt33sfse9dtgwr6a.streamlit.app/

## Overview

AI Career Advisor Chatbot is a conversational AI application that provides personalized career guidance, learning roadmaps, interview preparation tips, skill recommendations, and resume guidance.

The chatbot remembers important user information throughout the conversation and delivers responses tailored to the user's background, skills, and career goals.

---

## Features

* 💬 Interactive AI-powered career guidance
* 🧠 Conversation memory with context retention
* 🛣️ Personalized learning roadmaps
* 🎯 Skill recommendations based on career goals
* 📄 Resume and interview preparation guidance
* 🔄 Conversation summarization for long chats
* ⚠️ Error handling and logging
* ☁️ Deployed on Streamlit Cloud

---

## Tech Stack

* Python
* Streamlit
* LangChain
* Groq API (Llama 3.3 70B Versatile)
* Prompt Engineering
* Conversation Memory Management

---

## Project Structure

```text
career_advisor_chatbot/
│
├── app.py
├── requirements.txt
│
├── memory/
│   └── memory_manager.py
│
├── prompts/
│   └── career_prompt.py
│
├── services/
│   └── gemini_service.py
│
├── utils/
│   └── logger.py
```

---

## How It Works

1. User enters a career-related query.
2. The chatbot retrieves conversation context and memory.
3. LangChain constructs the prompt using user history.
4. Groq LLM generates a personalized response.
5. Important user information is summarized and stored.
6. Future responses use stored context for personalization.

---

## Example Use Cases

* Career planning
* AI Engineer roadmap
* Data Analyst roadmap
* Interview preparation
* Skill gap analysis
* Resume improvement
* Learning recommendations

---

## Deployment

The application is deployed on Streamlit Cloud:

https://careeradvisorchatbot-drqxrcyt33sfse9dtgwr6a.streamlit.app/

---

## Future Enhancements

* Resume Analyzer
* Job Recommendation Engine
* Vector Database Integration
* RAG-based Career Knowledge Base
* Multi-user Memory Support
* Authentication System

---

## Author

**Tejaswa Sadhu**

Computer Science Graduate | AI & Data Enthusiast

GitHub: https://github.com/tejassswa17
