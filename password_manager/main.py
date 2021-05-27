import bcrypt
import json

#BASIC SIGNUP FUNCTION WITH PASSWORD HASHING

#signup module
def signUp(usr):
    print('New Account Created')
    usr[username] = encryptme(user_password).decode('utf-8')
    
    writeUser(usr)
    return True

#Hashing of password
def encryptme(password):
    hashed_pass = bcrypt.hashpw(password.encode(),bcrypt.gensalt())
    return hashed_pass

#Checking if username already exists or not if username is already there than exit!
def checkUserExist(usr):
    if username in usr.keys():
        print("User Already Exists!")
        exit()

#login module
def login(usr):
    if username in usr.keys():
        if bcrypt.checkpw(user_password.encode(),usr[username].encode()):
            print(f"Welcome Back, {username}")
        else:
            print("Wrong Creds")
    else:
        print("Account Not Found!")


#READING USERS DATA AND IF FILE NOT FOUND CREATING ONE
def readUser():
    try:
        with open('pass.json','r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

#WRITING USERS IN JSON

def writeUser(usr):
    with open('pass.json','w+') as f:
        json.dump(users,f)

#Entry point
users = readUser()

#Main Menu
if __name__ == '__main__':
    print("WELCOME TO PASSWORD MANAGER!\n")
    menu = '''
        MENU:
            1. SIGNUP | PRESS(1) or (S)
            2. LOGIN | PRESS(2) or (L)
            3. EXIT | PRESS(3) or (E)'''
    while True:
        print(menu)
        usermenu_input = input("\nEnter Your Choice -> ").casefold()
        if usermenu_input == '1' or usermenu_input == 's'.casefold():           #if user enters 1 run Signup function
            username = input("Username -> ")
            checkUserExist(users)
            user_password = input("Password -> ")
            signUp(users)
            break
        elif usermenu_input == '2' or usermenu_input == 'l'.casefold():         #if user enters 2 run Login function
            username = input("Username -> ")
            user_password = input("Password -> ")
            login(users)
            break
        elif usermenu_input == '3' or usermenu_input == 'e'.casefold():         #if user enters 3 run Exit the program
            print("Thankyou For Using!")
            exit()
        else:
            print("Please Select From Given Options Only!")