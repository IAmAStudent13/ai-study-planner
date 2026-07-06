
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

OPENAI_API_KEY = ""

@app.route("/ai", methods=["POST"])
def ai():
    data = request.json
    query = data.get("query")

    response = requests.post(
        "https://api.openai.com/v1/chat/completions",
        headers={
            "Authorization": f"Bearer {OPENAI_API_KEY}",
            "Content-Type": "application/json"
        },
        json={
            "model": "gpt-4o-mini",
            "messages": [
                {"role": "system", "content": "You are a smart commerce study planner."},
                {"role": "user", "content": query}
            ]
        }
    )

    reply = response.json()["choices"][0]["message"]["content"]
    return jsonify({"response": reply})

if __name__ == "__main__":
    app.run(debug=True)
