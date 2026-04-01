import requests
from flask import Flask, request, jsonify

app = Flask(__name__)

# Hugging Face'dan olgan hf_...XpGN kodingizni shu yerga qo'ying
API_TOKEN = "hf_...XpGN" 
API_URL = "https://huggingface.co"
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def ai_assistant(message):
    try:
        payload = {"inputs": f"Siz aqlli yordamchisiz. Savol: {message}", "parameters": {"max_new_tokens": 200}}
        response = requests.post(API_URL, headers=headers, json=payload)
        output = response.json()
        return output[0]['generated_text'].split("Savol:")[-1].strip()
    except:
        return "Kechirasiz, hozircha javob bera olmayman."

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_msg = data.get("message")
    bot_reply = ai_assistant(user_msg)
    return jsonify({"reply": bot_reply})

if __name__ == '__main__':
    app.run(debug=True)
