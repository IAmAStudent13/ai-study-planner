
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

OPENAI_API_KEY = "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"

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
