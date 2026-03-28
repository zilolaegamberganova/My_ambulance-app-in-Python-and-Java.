from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# AI Robot mantiqi
def ai_assistant(message):
    message = message.lower()
    if "salom" in message:
        return "Assalomu alaykum! Men tez yordam AI yordamchisiman. Sizga qanday yordam kerak?"
    elif "yordam" in message or "tez" in message:
        return "Xavotir olmang, eng yaqin tez yordam mashinasini aniqlayapman. Manzilingizni yubora olasizmi?"
    elif "doktor" in message:
        return "Sizni hozir navbatchi shifokor bilan bog'layman."
    else:
        return "Tushunmadim, iltimos batafsilroq yozing. Sizga qanday yordam bera olaman?"

@app.route('/')
def index():
    # Templates papkasi ichidagi MY_index.html ni ochadi
    return render_template('MY_index.html')

@app.route('/chat', methods=['POST'])
def chat():
    data = request.get_json()
    user_message = data.get("message", "")
    bot_response = ai_assistant(user_message)
    return jsonify({"reply": bot_response})

if __name__ == '__main__':
    app.run()