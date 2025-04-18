import random
import itertools
from textwrap import dedent
import json
import os

logo2 = dedent("""
         ▐ ▄  ▄▄▄· .▄▄ · ▄▄▄▄▄ ▄· ▄▌     ▄▄▄· ▄▄▄· .▄▄ · .▄▄ · 
        •█▌▐█▐█ ▀█ ▐█ ▀. •██  ▐█▪██▌    ▐█ ▄█▐█ ▀█ ▐█ ▀. ▐█ ▀. 
        ▐█▐▐▌▄█▀▀█ ▄▀▀▀█▄ ▐█.▪▐█▌▐█▪     ██▀·▄█▀▀█ ▄▀▀▀█▄▄▀▀▀█▄
        ██▐█▌▐█ ▪▐▌▐█▄▪▐█ ▐█▌· ▐█▀·.    ▐█▪·•▐█ ▪▐▌▐█▄▪▐█▐█▄▪▐█
        ▀▀ █▪ ▀  ▀  ▀▀▀▀  ▀▀▀   ▀ •     .▀    ▀  ▀  ▀▀▀▀  ▀▀▀▀ 
""")

def print_section(title):
    print("=" * 80)
    print("{:^80}".format(title))
    print("=" * 80)

def prompt(label):
    print(f"[#] {label.ljust(40)}")
    return input(" |--> ").strip()

def print_formatted(text):
    print("{:80}".format(text))

def print_options(text):
    print(" "*4 + text)

def print_choise(options):
    return input(f"👉  Enter your choice {options} : ").strip()

def get_punctuation_by_level():
    level_1 = ['!', '@', '#', '$', '%', '&', '*', '_']
    level_2 = ['^', '-', '+', '=', '?']
    level_3 = ['"', "'", '(', ')', ',', '.', '/', ':', ';', '<', '>', '[', '\\', ']', '`', '{', '|', '}', '~']
    while True:
        try:
            level = int(input("{:45}".format("⚙️   Select punctuation level (1/2/3) :  ")))
            if level == 1:
                return level_1
            elif level == 2:
                return level_1 + level_2
            elif level == 3:
                return level_1 + level_2 + level_3
            else:
                print("Please enter 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Enter a number.")

def check_or_create_default_file():
    if not os.path.exists("default.json"):
        default_settings = {
            "length": 12,
            "use_lower": True,
            "use_upper": True,
            "use_digits": True,
            "use_punct": True,
            "punctuation_level": 2,
            "num_passwords": 5,
            "output_method": "print",
            "generation_mode": "1"
        }
        with open("default.json", "w") as f:
            json.dump(default_settings, f, indent=4)
        print("Created default.json with default settings.")

def load_default_settings():
    try:
        with open("default.json", "r") as f:
            return json.load(f)
    except Exception as e:
        print(f"Could not load default settings: {e}")
        return {}

def generate_passwords():
    print_section("🔐  Password Generator  🔐")
    print_formatted("[#] What would you like to do?")
    print_options("(1) Generate a new password")
    print_options("(2) Create a custom password")
    print_options("(3) Use a default password")
    choice = print_choise("(1/2/3)")

    if choice == "1":
        print_section("🔧  Password Configuration  🔧")
        length= int(input("{:45}".format("🔢  Password length :")))
        use_lower= input("{:45}".format("🔡  Include lowercase letters? (y/n) :")) == 'y'
        use_upper= input("{:45}".format("🔠  Include uppercase letters? (y/n) :")) == 'y'
        use_digits= input("{:45}".format("🔢  Include numbers? (y/n) :")) == 'y'
        use_punct= input("{:45}".format("🔣  Include punctuation? (y/n) :")) == 'y'

        characters = []
        if use_lower and use_upper:
            characters += list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        elif use_lower:
            characters += list("abcdefghijklmnopqrstuvwxyz")
        elif use_upper:
            characters += list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

        if use_digits:
            characters += list("0123456789")
        if use_punct:
            characters += get_punctuation_by_level()

        if not characters:
            print("You must select at least one character type.")
            return

        print_section("Generation Options")
        num_passwords = int(prompt("How many passwords to generate?"))
        output_method = prompt("Output method [print/file]:")
        generation_mode = prompt("Generation mode: random (1) or sequential (2)?:")

    elif choice == "3":
        print_section("Using Default Settings")
        settings = load_default_settings()
        length = settings.get("length", 12)
        use_lower = settings.get("use_lower", True)
        use_upper = settings.get("use_upper", True)
        use_digits = settings.get("use_digits", True)
        use_punct = settings.get("use_punct", False)
        punctuation_level = settings.get("punctuation_level", 1)
        num_passwords = settings.get("num_passwords", 5)
        output_method = settings.get("output_method", "print")
        generation_mode = settings.get("generation_mode", "1")

        characters = []
        if use_lower and use_upper:
            characters += list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ")
        elif use_lower:
            characters += list("abcdefghijklmnopqrstuvwxyz")
        elif use_upper:
            characters += list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")

        if use_digits:
            characters += list("0123456789")
        if use_punct:
            if punctuation_level == 1:
                characters += ['!', '@', '#', '$', '%', '&', '*', '_']
            elif punctuation_level == 2:
                characters += ['!', '@', '#', '$', '%', '&', '*', '_', '^', '-', '+', '=', '?']
            elif punctuation_level == 3:
                characters += ['!', '@', '#', '$', '%', '&', '*', '_', '^', '-', '+', '=', '?', '"', "'", '(', ')', ',', '.', '/', ':', ';', '<', '>', '[', '\\', ']', '`', '{', '|', '}', '~']

    elif choice == "2":
        print_section("Custom Password")
        print("Custom password feature not yet implemented.")
        return
    else:
        print("Invalid option.")
        return

    passwords = []
    if generation_mode == '1':
        for _ in range(num_passwords):
            password = ''.join(random.choice(characters) for _ in range(length))
            passwords.append(password)
    elif generation_mode == '2':
        all_combinations = itertools.product(characters, repeat=length)
        for i, comb in enumerate(all_combinations):
            if i >= num_passwords:
                break
            passwords.append(''.join(comb))

    print_section("Output")
    if output_method == 'print':
        for pwd in passwords:
            print(pwd)
    elif output_method == 'file':
        file_name = prompt("Enter the filename (with .txt extension):")
        with open(file_name, "w") as f:
            for pwd in passwords:
                f.write(pwd + "\n")
        print(f"\nPasswords saved to file: {file_name}")

if __name__ == "__main__":
    width = 80
    for line in logo2.splitlines():
        print(line.center(width))
    check_or_create_default_file()
    generate_passwords()
