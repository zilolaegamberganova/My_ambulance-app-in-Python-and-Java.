from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# --- Simulyatsiya qilingan bemor ma'lumotlari ---
PATIENT_INFO = {
    "name": "Ahsanul",
    "age": 25,
    "blood_type": "O+",
    "heart_rate": 76,
    "health_status": "94% Healthy",
}

# --- AI javobi simulyatsiya funksiyasi ---
def simulate_ai_response(user_message):
    user_message = user_message.lower()
    
    if "salom" in user_message:
        return f"Salom {PATIENT_INFO['name']}! Qalaysiz?"
    elif "qon" in user_message or "blood" in user_message:
        return f"Sizning qon turi {PATIENT_INFO['blood_type']}."
    elif "yurak" in user_message or "heart" in user_message:
        return f"Yurak urishi: {PATIENT_INFO['heart_rate']} BPM."
    elif "holat" in user_message or "status" in user_message:
        return f"Sog'liq holati: {PATIENT_INFO['health_status']}."
    elif user_message.strip() == "":
        return "Iltimos, savol yozing."
    else:
        return f"Simulyatsiya javob: Siz aytdingiz -> {user_message}"

# --- Asosiy sahifa ---
@app.route('/')
def index():
    return render_template('index.html')

# --- Chat API ---
@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.form.get("message", "")
    bot_reply = simulate_ai_response(user_message)
    return jsonify({"reply": bot_reply})

# --- Qo‘shimcha sahifalar ---
@app.route('/doctors')
def doctors():
    doctors_list = ["Dr. A. Smith", "Dr. B. Johnson", "Dr. C. Lee"]
    return render_template('doctors.html', doctors=doctors_list)

@app.route('/history')
def history():
    history_data = [
        {"date": "2026-04-01", "event": "Routine check-up, all normal"},
        {"date": "2026-03-28", "event": "Blood test, results fine"},
        {"date": "2026-03-15", "event": "Minor fever, treated with medication"},
    ]
    return render_template('history.html', history=history_data)

@app.route('/about')
def about():
    return render_template('about.html')

# --- Server ishga tushirish ---
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
