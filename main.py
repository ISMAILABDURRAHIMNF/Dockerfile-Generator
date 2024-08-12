from openai import OpenAI
client = OpenAI()

completion = client.chat.completions.create(
    model="gpt-4o-mini",
    messages=[
        {"role": "system", "content": "You are a helpful dockerfile generator"},
        {"role": "user", "content": "Create dockerfile content for a python project with flask, use latest technology, create a dockerfile content without any explanation"},
    ]
)

print(completion.choices[0].message.content)

#Main Menu
menu = {
    1: 'Python',
    2: 'PHP',
    3: 'JavaScript',
    4: 'Exit'
}

#Sub Menus (Version)
python_version = {
    1: 'Python 2',
    2: 'Python 3'
}

php_version = {
    1: 'PHP 5',
    2: 'PHP 7'
}

javascript_framework = {
    1: 'Angular',
    2: 'React',
    3: 'Vue.js',
    4: 'Node.js'
}


def show_menu(option=menu):
    for key, value in option.items():
        print(f'{key}. {value}')

def selected_option(*option):
    for item in option:
        print(f'You selected {item}')

#Sub Menus Function
def option_1():
    selected_option('Python')
    print('=== Select Python version ==')
    show_menu(python_version)
    version = int(input('Enter your choice: '))
    return version

def option_2():
    selected_option('PHP')
    print('=== Select PHP version ==')
    show_menu(php_version)
    version = int(input('Enter your choice: '))
    return version

def option_3():
    selected_option('JavaScript')
    print('=== Select JavaScript framework ==')
    show_menu(javascript_framework)
    version = int(input('Enter your choice: '))
    return version

#Main Function
def main():
    while True:
        print('\n=== Menu ===')
        show_menu()
        choice = int(input('Enter your choice: '))
        if choice == 1:
            version = option_1()
            selected_option("Python", python_version[version])
        elif choice == 2:
            version = option_2()
            selected_option("PHP", php_version[version])
        elif choice == 3:
            version = option_3()
            selected_option("JavaScript", javascript_framework[version])
        elif choice == 4:
            print('Thanks for using our application')
            break
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()