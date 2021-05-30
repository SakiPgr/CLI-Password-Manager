import json

PATH = "password_manager/pass.json"
MENU = '''
    MENU:
        1. Create Entry | PRESS(1) or (C)
        2. Show Entries | PRESS(2) or (S)
        3. Edit Entry   | PRESS(3) or (E)
        4. Delete Entry | PRESS(4) or (D)
        5. Exit Menu    | PRESS(5) or (E)'''

# The intended purpuse of this module is to allow the creating,
#  editing and deleting user data


class Entries():

    def __init__(self, user_name):
        self.user_name = user_name

    def get_entries(self):
        with open(PATH, "r+") as file:
            user_data = json.load(file)
        return user_data

    def write_file(self, new_user_data):
        with open(PATH, "w+") as file:
            json.dump(new_user_data, file, indent=4)

    def check_if_exists(self, website):
        user_data = self.get_entries()
        if website in user_data[self.user_name]["entries"].keys():
            return False
        else:
            return True

    def create_entry(self):
        user_data = self.get_entries()
        website = input("\nPlease enter the website -> ")
        if self.check_if_exists(website=website):
            password = input("\nPlease enter the password -> ")
            user_data[self.user_name]["entries"][website] = password
            self.write_file(user_data)
        else:
            print("This entry already exists.")
            input("Please press enter to continue to menu.")

    def show_existing_entries(self):
        with open(PATH, "r") as file:
            user_data = json.load(file)
            entries = user_data[self.user_name]["entries"]
            for key, value in entries.items():
                print(f"Entry: {key}, Password: {value}")

    def edit_entry(self):
        user_data = self.get_entries()
        website = input("\nWhich entry do you want to edit?\n")
        if not self.check_if_exists(website=website):
            new_password = input("Please enter the new password.\n")
            user_data[self.user_name]["entries"][website] = new_password
            self.write_file(user_data)
        else:
            print("This entry does not exist.")

    def delete_entry(self):
        user_data = self.get_entries()
        self.show_existing_entries()
        website = input("\nPlease enter the entry you want to delete.\n")
        if not self.check_if_exists(website):
            del user_data[self.user_name]["entries"][website]
        self.write_file(user_data)

    def menu(self):
        while True:
            print(MENU)
            user_choice = input("\nPlease enter your choice -> \n").casefold()
            if user_choice == '1' or user_choice == 'c'.casefold():
                self.create_entry()
            elif user_choice == '2' or user_choice == 's'.casefold():
                self.show_existing_entries()
                input("\nPlease press enter to continue to Menu.")
            elif user_choice == '3' or user_choice == 'e'.casefold():
                self.edit_entry()
            elif user_choice == '4' or user_choice == 'd'.casefold():
                self.delete_entry()
            elif user_choice == '5' or user_choice == 'q'.casefold():
                break
            else:
                print("Please select from given options only!")
