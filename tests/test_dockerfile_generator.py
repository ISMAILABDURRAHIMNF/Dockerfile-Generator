import unittest
from unittest.mock import patch
from io import StringIO
import sys

sys.path.append('./')
from dockerfile_generator import generate_dockerfile

class TestGenerateDockerfile(unittest.TestCase):

    @patch('dockerfile_generator.client.chat.completions.create')
    @patch('sys.stdout', new_callable=StringIO)
    def test_generate_dockerfile_template(self, mock_stdout, mock_create):
        language = "Python"
        version = "Python 3.9"

        # Panggil fungsi generate_dockerfile
        generate_dockerfile(language, version)

        # Memeriksa output dari print pertama
        output = mock_stdout.getvalue().splitlines()
        expected_first_print = f"\n\nGenerating Dockerfile for {language} using {version} project..."
        self.assertEqual(f'\n\n{output[2]}', expected_first_print)

        # Memeriksa project_description
        expected_description = f"{language} project with {version} version"
        self.assertEqual(
            mock_create.call_args[1]['messages'][1]['content'],
            f"Create Dockerfile content for a {expected_description}, use latest technology, create a Dockerfile content without any explanation"
        )

if __name__ == '__main__':
    unittest.main()
