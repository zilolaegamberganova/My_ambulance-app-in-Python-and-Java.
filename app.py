import requests
import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# --- HUGGING FACE AI SOZLAMALARI ---
# Bu model ko'p tillarni (UZ, EN, RU) yaxshi tushunadi
API_URL = "https://huggingface.co"
API_TOKEN = "hf_XpGN..." # O'zingizning to'liq tokiningizni qo'ying

headers = {"Authorization": f"Bearer {API_TOKEN}"}

def ai_assistant(message):
    try:
        payload = {"inputs": message}
        response = requests.post(API_URL, headers=headers, json=payload)
        output = response.json()
        
        # AI javobini olish
        if isinstance(output, list):
            return output[0]['generated_text']
        else:
            return output.get('generated_text', "I am thinking... Please try again.")
    except:
        return "Sorry, I'm having trouble connecting to my brain right now."

@app.route('/')
def index():
    # MUHIM: Fayl nomi 'index.html' bo'lishi kerak, 'MY_index.html' emas!
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    
    # AI ga xabarni yuboramiz
    bot_response = ai_assistant(user_message)
    
    return jsonify({"reply": bot_response})

if __name__ == '__main__':
    # Render platformasida ishlashi uchun portni sozlaymiz
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
