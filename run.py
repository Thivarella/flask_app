import os
from flask import Flask
from app import api_bp
from models.Model import db

app = Flask(__name__)
app.config.from_object("config")

app.register_blueprint(api_bp)

db.init_app(app)


if __name__ == "__main__":
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port)
