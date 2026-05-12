from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from openai import OpenAI
import datetime
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=os.environ.get("OPENROUTER_API_KEY")
)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/command', methods=['POST'])
def handle_command():
    try:
        data = request.json
        command = data.get('command', '').lower().strip()

        if not command:
            return jsonify({"response": "I didn't receive any command sir."})

        if "open google" in command:
            return jsonify({"response": "Opening Google sir.", "url": "https://www.google.com"})
        elif "open youtube" in command:
            return jsonify({"response": "Opening YouTube sir.", "url": "https://www.youtube.com"})
        elif "open facebook" in command:
            return jsonify({"response": "Opening Facebook sir.", "url": "https://www.facebook.com"})
        elif "open instagram" in command:
            return jsonify({"response": "Opening Instagram sir.", "url": "https://www.instagram.com"})
        elif "what time" in command:
            now = datetime.datetime.now().strftime("%I:%M %p")
            return jsonify({"response": f"The current time is {now} sir."})
        elif "what date" in command or "today date" in command:
            today = datetime.datetime.now().strftime("%B %d, %Y")
            return jsonify({"response": f"Today is {today} sir."})
        else:
            completion = client.chat.completions.create(
                extra_headers={
                    "HTTP-Referer": "https://jarvis-python-project.onrender.com/",
                    "X-Title": "Jarvis",
                },
                model="openai/gpt-4o-mini",
                messages=[
                    {"role": "system", "content": "You are Jarvis. Reply in ONE short sentence like a butler."},
                    {"role": "user", "content": command}
                ]
            )
            response = completion.choices[0].message.content
            return jsonify({"response": response})

    except Exception as e:
        return jsonify({"response": f"Sorry sir, error: {str(e)}"}), 500

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)