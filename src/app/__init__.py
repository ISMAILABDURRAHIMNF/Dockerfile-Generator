"""__init__ file"""

import os
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv
from .handler import handler

load_dotenv()

def create_app():
    """Blueprint and routing"""

    app = Flask(__name__)

    app.secret_key = os.getenv('SECRET_KEY')

    CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})
    app.register_blueprint(handler)

    return app
