"""Route Handler"""

import os
from flask import Blueprint, request, jsonify, send_from_directory
from .dockerfile_generator import generate_dockerfile

handler = Blueprint('handler', __name__)

PATH = os.getenv('DEPLOY_PATH')

@handler.route('/', methods=['GET'])
def hello():
    """General message"""

    return jsonify({'message': 'Ini API Dockerfile Generator'}), 200

@handler.route('/generate', methods=['POST'])
def index():
    """Generate and saving into the file"""

    file = request.files.get('file')
    language = request.form.get('language').lower()
    desc = request.form.get('desc')

    app_name = file.filename.replace(".zip","")
    folder_deploy = f'{PATH}{app_name}'

    os.makedirs(folder_deploy)

    dockerfile_content = generate_dockerfile(language, desc)

    with open(f'{folder_deploy}/Dockerfile', 'w', encoding="utf-8") as file :
        file.write(dockerfile_content)

    return jsonify({'message': 'Generate berhasil!', 'dockerfile': dockerfile_content}), 200

@handler.route('/download', methods=['POST'])
def download():
    """Download dockerfile"""

    app_name = request.get_json()['app_name']

    return send_from_directory(f'{PATH}{app_name}','Dockerfile', as_attachment=True)
