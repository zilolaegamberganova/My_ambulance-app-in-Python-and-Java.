from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/ask_ai', methods=['POST'])
def ask_ai():
    data = request.json
    user_msg = data.get('message')
    lang = data.get('lang')

    # Bu yerda AI modeliga (masalan OpenAI) murojaat qilish mumkin
    # Hozircha oddiy test javobi qaytaramiz:
    if lang == 'uz':
        reply = f"AI javobi: Siz '{user_msg}' dedingiz."
    elif lang == 'en':
        reply = f"AI Response: You said '{user_msg}'."
    else:
        reply = f"Ответ ИИ: Вы сказали '{user_msg}'."

    return jsonify({"reply": reply})

if __name__ == '__main__':
    app.run(debug=True)
