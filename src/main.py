from flask import Flask, render_template, request, jsonify
from flask_cors import CORS
from src.chatbot import chatbot_response  # relative import

app = Flask(__name__)
CORS(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/ask", methods=["POST"])
def ask():
    data = request.get_json()
    user_input = data.get("message")
    user_id = data.get("user_id", "default")
    if not user_input:
        return jsonify({"error": "No input"}), 400
    response_text = chatbot_response(user_id)
    return jsonify({"response": response_text})

if __name__ == "__main__":
    app.run(debug=True)
