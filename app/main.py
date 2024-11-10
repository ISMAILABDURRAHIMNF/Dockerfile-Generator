from flask import Blueprint, request, jsonify
from .dockerfile_generator import generate_dockerfile
import os

main = Blueprint('main', __name__)

PATH = 'D:/Mini Project/File_Deploy/'

# def hitung_file():
#         items = os.listdir(PATH)
#         jumlah_folder = 0
#         for item in items:
#                 path_item = f'{PATH}/{item}'
#                 if os.path.isdir(path_item):
#                         jumlah_folder += 1
#         return jumlah_folder

@main.route('/generate', methods=['POST'])
def index():
        file = request.files.get('file')
        language = request.form.get('language').lower()
        version = request.form.get('version')

        folder_deploy = f'{PATH}/Folder_{file.filename}'
        os.makedirs(folder_deploy)
     
        dockerfile_content = generate_dockerfile(language, version)

        # nomor = hitung_file()

        with open(f'{folder_deploy}/Dockerfile', 'w') as file :
                file.write(dockerfile_content)

        return jsonify({'message': 'Generate berhasil!', 'dockerfile': dockerfile_content})

# menu = {
#     1: 'Python',
#     2: 'PHP',
#     3: 'JavaScript',
#     4: 'Exit'
# }

# python_version = {
#     1: 'Python 3.8',
#     2: 'Python 3.9',
#     3: 'Python 3.10',
#     4: 'Python 3.11',
#     5: 'Python 3.12',
#     6: 'Python 3.13'
# }

# php_version = {
#     1: 'PHP 7.0',
#     2: 'PHP 7.1',
#     3: 'PHP 7.2',
#     4: 'PHP 7.3',
#     5: 'PHP 7.4',
#     6: 'PHP 8.0',
#     7: 'PHP 8.1',
#     8: 'PHP 8.2',
#     9: 'PHP 8.3'
# }

# javascript_framework = {
#     1: 'Angular',
#     2: 'React',
#     3: 'Vue.js',
#     4: 'Node.js',
#     5: 'Next.js',
# }