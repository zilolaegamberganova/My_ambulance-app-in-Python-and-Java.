import requests
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

# Hugging Face API sozlamalari (O'zingizniki tursin)
API_TOKEN = "hf_...XpGN" 
API_URL = "https://huggingface.co" # Model manzili aniq bo'lishi kerak
headers = {"Authorization": f"Bearer {API_TOKEN}"}

def ai_assistant(message):
    try:
        payload = {"inputs": message, "parameters": {"max_new_tokens": 100}}
        response = requests.post(API_URL, headers=headers, json=payload)
        output = response.json()
        # Hugging Face'dan keladigan javobni to'g'ri olish
        return output[0]['generated_text'] if isinstance(output, list) else "Xatolik yuz berdi."
    except:
        return "Kechirasiz, hozircha javob bera olmayman."

# 1. BU MUHIM: HTML sahifangiz ochilishi uchun kerak
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.json
    user_msg = data.get("message")
    # 2. BU YERDA: Til ma'lumotini ham qabul qilishimiz mumkin
    bot_reply = ai_assistant(user_msg)
    return jsonify({"reply": bot_reply})

if __name__ == '__main__':
    app.run(debug=True)
