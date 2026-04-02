import requests
import os
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# --- HUGGING FACE SOZLAMALARI ---
# Modelni aniq ko'rsatish kerak (Blenderbot suhbat uchun juda yaxshi)
API_URL = "https://huggingface.co"
API_TOKEN = "hf_XpGN..." # O'zingizning to'liq tokiningizni qo'ying
headers = {"Authorization": f"Bearer {API_TOKEN}"}

# Bemor haqida ma'lumot (AI tahlil qilishi uchun)
PATIENT_CONTEXT = """
Patient Name: Ahsanul. 
Age: 25. 
Blood Type: O+. 
Heart Rate: 76 BPM (Normal). 
Health Status: 94% Healthy.
System: Ambulance AI Dashboard.
"""

def ai_assistant(message):
    try:
        # AIga kontekst beramiz: u kim bilan gaplashayotganini bilsin
        prompt = f"Context: {PATIENT_CONTEXT} User asks: {message}"
        
        payload = {"inputs": prompt}
        response = requests.post(API_URL, headers=headers, json=payload)
        output = response.json()
        
        # Hugging Face javobini qayta ishlash
        if isinstance(output, list) and len(output) > 0:
            return output[0].get('generated_text', "I'm processing that...")
        elif isinstance(output, dict):
            return output.get('generated_text', "Let me think about that.")
        return "I'm ready to help you, Ahsanul!"
    except:
        return "System busy, but I'm monitoring your vitals, Ahsanul."

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    
    # AI javobi
    bot_response = ai_assistant(user_message)
    
    return jsonify({"reply": bot_response})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
