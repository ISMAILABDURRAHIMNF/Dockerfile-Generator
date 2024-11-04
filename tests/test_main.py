import unittest
from unittest.mock import patch
from io import StringIO
import sys

sys.path.append('./')
from main import main

class TestMain(unittest.TestCase):
    def test_invalid_language(self):
        with patch('builtins.input', side_effect=[5, 4]) as mock_input, patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()
            self.assertEqual(output, '\n=== Menu ===\n1. Python\n2. PHP\n3. JavaScript\n4. Exit\nInvalid language\n\n=== Menu ===\n1. Python\n2. PHP\n3. JavaScript\n4. Exit\nThanks for using our application\n')

    def test_python_language(self):
        with patch('builtins.input', side_effect=[1, 1, 4]) as mock_input, patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()
            self.assertEqual(output, '\n=== Menu ===\n1. Python\n2. PHP\n3. JavaScript\n4. Exit\n=== Select Python Version ===\n1. Python 3.8\n2. Python 3.9\n3. Python 3.10\n4. Python 3.11\n5. Python 3.12\n6. Python 3.13\n\n\nGenerating Dockerfile for Python using Python 3.8 project...\n\n\n=== Dockerfile generated successfully ===\n\n\n\n=== Menu ===\n1. Python\n2. PHP\n3. JavaScript\n4. Exit\nThanks for using our application\n')

    def test_php_language(self):
        with patch('builtins.input', side_effect=[2, 1, 4]) as mock_input, patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()
            self.assertEqual(output, '\n=== Menu ===\n1. Python\n2. PHP\n3. JavaScript\n4. Exit\n=== Select PHP Version ===\n1. PHP 7.0\n2. PHP 7.1\n3. PHP 7.2\n4. PHP 7.3\n5. PHP 7.4\n6. PHP 8.0\n7. PHP 8.1\n8. PHP 8.2\n9. PHP 8.3\n\n\nGenerating Dockerfile for PHP using PHP 7.0 project...\n\n\n=== Dockerfile generated successfully ===\n\n\n\n=== Menu ===\n1. Python\n2. PHP\n3. JavaScript\n4. Exit\nThanks for using our application\n')

    def test_javascript_language(self):
        with patch('builtins.input', side_effect=[3, 1, 4]) as mock_input, patch('sys.stdout', new_callable=StringIO) as mock_stdout:
            main()
            output = mock_stdout.getvalue()
            self.assertEqual(output, '\n=== Menu ===\n1. Python\n2. PHP\n3. JavaScript\n4. Exit\n=== Select Javascript Framework ===\n1. Angular\n2. React\n3. Vue.js\n4. Node.js\n5. Next.js\n\n\nGenerating Dockerfile for JavaScript using Angular project...\n\n\n=== Dockerfile generated successfully ===\n\n\n\n=== Menu ===\n1. Python\n2. PHP\n3. JavaScript\n4. Exit\nThanks for using our application\n')

if __name__ == '__main__':
    unittest.main()