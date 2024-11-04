import unittest
from unittest.mock import patch
from io import StringIO
import sys

sys.path.append('./')
from menu import show_menu, show_main_menu, select_option


class TestShowMenu(unittest.TestCase):
    @patch('sys.stdout', new_callable=StringIO)
    def test_show_menu(self, mock_stdout):
        test_menu = {
            1: 'Python',
            2: 'PHP',
            3: 'JavaScript',
            4: 'Exit'
        }

        show_menu(option=test_menu)

        expected_output = '1. Python\n2. PHP\n3. JavaScript\n4. Exit\n'

        self.assertEqual(mock_stdout.getvalue(), expected_output)
        

class TestShowMainMenu(unittest.TestCase):
    expected_language = {
        1: 'Python',
        2: 'PHP',
        3: 'JavaScript',
        4: 'Exit'
    }

    def test_show_main_menu(self, expected_language=expected_language):
        for i, expected in enumerate(expected_language, start=1):
            with patch('builtins.input', side_effect=[i]) as mock_input, patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                result = show_main_menu()
                output = mock_stdout.getvalue()
                self.assertEqual(output, '\n=== Menu ===\n1. Python\n2. PHP\n3. JavaScript\n4. Exit\n')
                mock_input.assert_called_with('Enter your language: ')
                self.assertEqual(result, expected)

class TestSelectOption(unittest.TestCase):
    expected_results_py = [
        'Python 3.8', 
        'Python 3.9', 
        'Python 3.10', 
        'Python 3.11', 
        'Python 3.12', 
        'Python 3.13'
    ]

    expected_results_php = [
        'PHP 7.0', 
        'PHP 7.1', 
        'PHP 7.2', 
        'PHP 7.3', 
        'PHP 7.4', 
        'PHP 8.0',
        'PHP 8.1',
        'PHP 8.2',
        'PHP 8.3'
    ]

    expected_results_js = [
        'Angular',
        'React',
        'Vue.js',
        'Node.js',
        'Next.js'
    ]

    def test_python_option(self, expected_results=expected_results_py):
        with patch('builtins.input', side_effect=[1, 2, 3, 4, 5, 6]):
            for i, expected in enumerate(expected_results, start=1):
                result = select_option("Select Python Version")
                self.assertEqual(result, expected)

    def test_php_option(self, expected_results=expected_results_php):
        with patch('builtins.input', side_effect=[1, 2, 3, 4, 5, 6, 7, 8, 9]):
            for i, expected in enumerate(expected_results, start=1):
                result = select_option("Select PHP Version")
                self.assertEqual(result, expected)

    def test_javascript_option(self, expected_results=expected_results_js):
        with patch('builtins.input', side_effect=[1, 2, 3, 4, 5]):
            for i, expected in enumerate(expected_results, start=1):
                result = select_option("Select Javascript Framework")
                self.assertEqual(result, expected)

    def test_input_version(self, expected_results=expected_results_py):
        for i, expected in enumerate(expected_results, start=1):
            with patch('builtins.input', side_effect=[i]) as mock_input, patch('sys.stdout', new_callable=StringIO) as mock_stdout:
                    result = select_option("Select Python Version")
                    output = mock_stdout.getvalue()
                    self.assertEqual(output, '=== Select Python Version ===\n1. Python 3.8\n2. Python 3.9\n3. Python 3.10\n4. Python 3.11\n5. Python 3.12\n6. Python 3.13\n')
                    mock_input.assert_called_with('Enter your language: ')
                    self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()