from flask import Flask, request, jsonify
from flask_cors import CORS
import requests
import os

app = Flask(__name__)
CORS(app)

GEMINI_API_KEY = "AIzaSyD1Cv2q5NYCv42-VvyDYjdsMt1eDQIRy0I"  # replace with your key

@app.route('/generate-quiz', methods=['POST'])
def generate_quiz():
    data = request.json
    language = data.get('language', 'Python')
    level = data.get('level', 'easy')

    prompt = f"Generate 5 {level} level multiple-choice questions for {language}. Each question should have 4 options and mention the correct answer."

    url = f"https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent?key={GEMINI_API_KEY}"

    try:
        response = requests.post(url, json={
            "contents": [{"parts": [{"text": prompt}]}]
        })
        print("Gemini response:", response.json())  # Add this line

        result = response.json()
        text = result.get("candidates", [{}])[0].get("content", {}).get("parts", [{}])[0].get("text", "No content returned.")
        return jsonify({"content": text})

    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
