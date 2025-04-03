import os
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

OPENROUTER_API_KEY = os.environ.get("OPENROUTER_API_KEY")

@app.route('/chat', methods=['POST'])
def chat():
    messages = request.json.get('messages', [])

    headers = {
        "Authorization": f"Bearer {OPENROUTER_API_KEY}",
        "Content-Type": "application/json"
    }

    data = {
        "model": "openai/gpt-3.5-turbo",  # or another OpenRouter-supported model
        "messages": messages
    }

    try:
        response = requests.post("https://openrouter.ai/api/v1/chat/completions", headers=headers, json=data)
        response.raise_for_status()
        reply = response.json()["choices"][0]["message"]["content"]
        return jsonify({ "reply": reply })
    except Exception as e:
        print("Error:", e)
        return jsonify({ "reply": "Something went wrong talking to Ai." })
