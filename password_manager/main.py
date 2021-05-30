# Let's rock
import bcrypt
import json
from edit_user_data import Entries
import getpass

# BASIC SIGNUP FUNCTION WITH PASSWORD HASHING


# signup module
def sign_up(usr):
    print('New Account Created')
    # I changed this line so that the json file can be used to
    # save the websites and passwords too.
    usr[username] = {
        "password": encrypt_me(user_password).decode('utf-8'),
        "entries": {}
    }
    write_user(usr)
    return True


# Hashing of password
def encrypt_me(password):
    hashed_pass = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    return hashed_pass


# Checking if username already exists or
# not if username is already there than exit!
def check_user_exist(usr):
    if username in usr.keys():
        print("Account Already Exists!")
        print("Please try again.")


# login module
def login(usr):
    if username in usr.keys():
        if bcrypt.checkpw(user_password.encode(), usr[username]['password'].encode()):
            print(f"Welcome Back, {username}")
            # Created this line to get to the entries menu
            user = Entries(username)
            user.menu()
        else:
            print("Wrong Password")
    else:
        print("Account Not Found!")


# READING USERS DATA AND IF FILE NOT FOUND CREATING ONE
def read_user():
    try:
        with open('password_manager/pass.json', 'r') as f:
            return json.load(f)
    except json.decoder.JSONDecodeError:
        return {}
    except FileNotFoundError:
        return {}


# WRITING USERS IN JSON
def write_user(usr):
    with open('password_manager/pass.json', 'w+') as f:
        json.dump(users, f, indent=4)


# Entry point
users = read_user()

# Main Menu
if __name__ == '__main__':
    print("WELCOME TO PASSWORD MANAGER!\n")
    menu = '''
        MENU:
            1. SIGNUP | PRESS(1) or (S)
            2. LOGIN  | PRESS(2) or (L)
            3. EXIT   | PRESS(3) or (Q)'''
    while True:
        print(menu)
        user_choice = input("\nPlease enter your choice -> ").casefold()
        # if user enters 1 run Signup function
        if user_choice == '1' or user_choice == 's'.    casefold():
            username = input("Username -> ")
            check_user_exist(users)
            user_password = getpass.getpass("Password -> ")
            sign_up(users)
        # if user enters 2 run Login function
        elif user_choice == '2' or user_choice == 'l'.casefold():
            username = input("Username -> ")
            user_password = getpass.getpass("Password -> ")
            login(users)
        # if user enters 3 run Exit the program
        elif user_choice == '3' or user_choice == 'q'.casefold():
            print("Thank you for using PASSWORD MANAGER!")
            exit()
        else:
            print("Please select from given options only!")
