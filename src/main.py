import os
from flask import Flask, render_template
from src.communication.web_app import web_bp
from src.communication.sms_handler import sms_bp
from src.communication.whatsapp_bot import whatsapp_bp

BASE_DIR = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")
STATIC_DIR = os.path.join(BASE_DIR, "static")

print("Template dir:", TEMPLATE_DIR)   # 👈 Debug
print("Static dir:", STATIC_DIR)

app = Flask(__name__, template_folder=TEMPLATE_DIR, static_folder=STATIC_DIR)

# Register blueprints
app.register_blueprint(web_bp)
app.register_blueprint(sms_bp)
app.register_blueprint(whatsapp_bp)

@app.route("/")
def index():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
