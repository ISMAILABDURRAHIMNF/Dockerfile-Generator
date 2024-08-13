menu = {
    1: 'Python',
    2: 'PHP',
    3: 'JavaScript',
    4: 'Exit'
}

python_version = {
    1: 'Python 3.8',
    2: 'Python 3.9',
    3: 'Python 3.10',
    4: 'Python 3.11',
    5: 'Python 3.12',
    6: 'Python 3.13'
}

php_version = {
    1: 'PHP 7.0',
    2: 'PHP 7.1',
    3: 'PHP 7.2',
    4: 'PHP 7.3',
    5: 'PHP 7.4',
    6: 'PHP 8.0',
    7: 'PHP 8.1',
    8: 'PHP 8.2',
    9: 'PHP 8.3'
}

javascript_framework = {
    1: 'Angular',
    2: 'React',
    3: 'Vue.js',
    4: 'Node.js',
    5: 'Next.js',
}

def show_menu(option=menu):
    for key, value in option.items():
        print(f'{key}. {value}')

def show_main_menu():
    print('\n=== Menu ===')
    show_menu()
    choice = int(input('Enter your choice: '))
    return choice

def select_option(title):
    if title == "Select Python Version":
        options = python_version
    elif title == "Select PHP Version":
        options = php_version
    elif title == "Select Javascript Framework":
        options = javascript_framework
    else:
        options = {}

    print(f"=== {title} ===")
    show_menu(options)
    version = int(input('Enter your choice: '))
    return options[version]