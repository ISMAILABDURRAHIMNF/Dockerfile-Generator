from flask import Flask
from dotenv import load_dotenv
from .main import main
from flask_cors import CORS
import os

load_dotenv()

def create_app():
    app = Flask(__name__)

    app.secret_key = os.getenv('SECRET_KEY')
    
    CORS(app, resources={r"/*": {"origins": "http://localhost:5173"}})
    app.register_blueprint(main)

    return app