# ilya khenkin 43/3 final project

from main_menu import main_menu  # getting a module with main menu function


def main():

    command = 0  # start value for while
    while command != '6':
        print("\nWelcome to the Security System")
        print("1 - Get camera data.")
        print("2 - Get last camera photo.")
        print("3 - Get all aren't same types of cameras.")
        print("4 - Calculate degrees.")
        print("5 - Get cameras with a same names.")
        print("6 - Exit.")
        command = input("Write here command number:>> ")
        if(command != '6'):
            main_menu(command)
        else:
            print("\n\n--------------------------------")
            print("Thank you for using our program.")
            print("--------------------------------")


if __name__ == '__main__':
    main()
