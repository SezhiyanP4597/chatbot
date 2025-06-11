# 💬 Chatbot template

A simple Streamlit app that shows how to build a chatbot using OpenAI's GPT-3.5.

[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://chatbot-template.streamlit.app/)

### How to run it on your own machine

# File structure:
# planto-support/
# ├── app.py
# ├── requirements.txt
# ├── Dockerfile
# └── README.md
```  

# README.md  
```markdown
# Planto.ai Customer Support Chatbot (Gemini AI)

This project implements a customer-support chatbot for the Planto.ai website using Google Gemini AI agents, deployed via Streamlit and containerized with Docker. All services use free-tier subscriptions.

## Prerequisites
- Python 3.8+
- Free Google Cloud API key with Vertex AI enabled (sign up at https://cloud.google.com/ and enable Vertex AI)
- Docker (for containerization)

## Setup in VS Code
1. Clone this repo and open in VS Code.
2. Create a virtual environment: `python -m venv venv` and activate it.
3. Install dependencies: `pip install -r requirements.txt`.
4. Create a `.env` file with your Google API key:
   ```ini
   GOOGLE_API_KEY=your_google_api_key_here
   ```
5. Enable the Vertex AI API in your Google Cloud project and grant your API key access.
6. Run the app locally: `streamlit run app.py`.

## Building & Running with Docker
```sh
# Build the image
docker build -t planto-support-app-gemini .

# Run the container
docker run -e GOOGLE_API_KEY=$GOOGLE_API_KEY -p 8501:8501 planto-support-app-gemini
```

Then visit `http://localhost:8501`.
```  
