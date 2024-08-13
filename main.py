from menu import show_main_menu, select_option
from dockerfile_generator import generate_dockerfile

def main():
    while True:
        choice = show_main_menu()

        if choice == 1:
            version = select_option("Select Python Version")
            generate_dockerfile("Python", version)
        elif choice == 2:
            version = select_option("Select PHP Version")
            generate_dockerfile("PHP", version)
        elif choice == 3:
            version = select_option("Select Javascript Framework")
            generate_dockerfile("JavaScript", version)
        elif choice == 4:
            print('Thanks for using our application')
            break
        else:
            print('Invalid choice')

if __name__ == '__main__':
    main()
