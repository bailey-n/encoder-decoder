class Password:
    def __init__(self):
        self.commands = [self.encode_password, self.decode_password, self.quit]
        self.isRunning = True
        self.password = None

    def encode_password(self):
        self.password = input(f"Please enter your password to encode: ")
        self.password = encode(self.password)
        print("Your password has been encoded and stored!\n")

    def decode_password(self):
        print(f"The encoded password is {self.password}, and the original password is {decode(self.password)}.")

    def quit(self):
        self.isRunning = False

    def get_menu_input(self):
        getting_input = True
        option = None
        while getting_input:
            print(f"Menu\n"
                  f"-------------\n"
                  f"1. Encode\n"
                  f"2. Decode\n"
                  f"3. Quit\n")
            option = input(f"Please enter an option: ")
            try:
                option = int(option) - 1
                if option in range(3):
                    getting_input = False
                else:
                    print("Invalid option!\n")
            except:
                print("Invalid option!\n")
        return self.commands[option]


def encode(password_str):
    return ""
    # return "".join(str((int(char) + 3) % 10) for char in password_str)


def decode(password_str):
    return ""
    # return "".join(str((int(char) - 3) % 10) for char in password_str)


if __name__ == "__main__":
    password = Password()
    while password.isRunning:
        command = password.get_menu_input()
        command()

