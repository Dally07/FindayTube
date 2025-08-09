from flask import Flask
from app.routes.controls import bp

app = Flask(__name__, template_folder="app/templates")
app.register_blueprint(bp)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
