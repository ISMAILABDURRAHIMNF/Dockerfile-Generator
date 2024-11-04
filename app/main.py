from flask import Blueprint, request, jsonify
from .dockerfile_generator import generate_dockerfile

main = Blueprint('main', __name__)

@main.route('/generate', methods=['POST'])
def index():
        language = request.form['language'].lower()
        version = request.form['version']
        dockerfile_content = generate_dockerfile(language, version)

        return jsonify({'message': 'Generate berhasil!', 'dockerfile': dockerfile_content})