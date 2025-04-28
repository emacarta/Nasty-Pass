# Libreries 

import random
import secrets
import itertools
from textwrap import dedent
import json
import os

# Data 

logo = dedent("""
         ▐ ▄  ▄▄▄· .▄▄ · ▄▄▄▄▄ ▄· ▄▌     ▄▄▄· ▄▄▄· .▄▄ · .▄▄ · 
        •█▌▐█▐█ ▀█ ▐█ ▀. •██  ▐█▪██▌    ▐█ ▄█▐█ ▀█ ▐█ ▀. ▐█ ▀. 
        ▐█▐▐▌▄█▀▀█ ▄▀▀▀█▄ ▐█.▪▐█▌▐█▪     ██▀·▄█▀▀█ ▄▀▀▀█▄▄▀▀▀█▄
        ██▐█▌▐█ ▪▐▌▐█▄▪▐█ ▐█▌· ▐█▀·.    ▐█▪·•▐█ ▪▐▌▐█▄▪▐█▐█▄▪▐█
        ▀▀ █▪ ▀  ▀  ▀▀▀▀  ▀▀▀   ▀ •     .▀    ▀  ▀  ▀▀▀▀  ▀▀▀▀ 
""")


letter_variants = {
    'a': ['A', '@', '4'],
    'b': ['B', '8'],
    'c': ['C', '(', '<'],
    'd': ['D'],
    'e': ['E', '3'],
    'f': ['F'],
    'g': ['G', '9', '6'],
    'h': ['H', '#'],
    'i': ['I', '1', '!', '|'],
    'j': ['J'],
    'k': ['K'],
    'l': ['L', '1', '|'],
    'm': ['M'],
    'n': ['N'],
    'o': ['O', '0'],
    'p': ['P'],
    'q': ['Q', '9'],
    'r': ['R'],
    's': ['S', '$', '5'],
    't': ['T', '7', '+'],
    'u': ['U', 'v'],
    'v': ['V', 'u', 'U'],
    'w': ['W', 'm', 'M'],
    'x': ['X', '%', '*'],
    'y': ['Y'],
    'z': ['Z', '2']
}


# Functions

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
    return input(f"👉  Enter your choice {options} : ")


def list_to_string(symbols, per_line=10):
    lines = []
    for i in range(0, len(symbols), per_line):
        chunk = symbols[i:i+per_line]
        lines.append("  ".join(chunk))
    return "\n".join(lines)


def get_punctuation_by_level():
    level_1 = ['!', '@', '#', '$', '%', '&', '*', '_']
    level_2 = ['^', '-', '+', '=', '?']
    level_3 = ['"', "'", '(', ')', ',', '.', '/', ':', ';', '<', '>', '[', '\\', ']', '`', '{', '|', '}', '~']
    
    # Creiamo le stringhe
    str_level_1 = list_to_string(level_1)
    str_level_2 = list_to_string(level_2)
    str_level_3 = list_to_string(level_3)

    # Stampa grafica carina
    print("-" * 80)
    print("{:^80}".format("🔣  Punctuation Levels"))
    print("-" * 80)

    print("{:45}".format(f"🔸 Level 1 (Basic)"))
    print("{:^80}".format(str_level_1))

    print("{:45}".format(f"\n🔸 Level 2 (Intermediate)"))
    print("{:^80}".format(str_level_2))

    print("{:45}".format(f"\n🔸 Level 3 (Extended)"))
    print("{:^80}".format("error in visualizaion"))
    #print("{:^80}".format(str_level_3[:5]))

    while True:
        try:
            level = ask_number(f"\n⚙️  - Select punctuation level","(1/2/3)",1,3 )
            #level = int(input("{:45}".format("\n⚙️  - Select punctuation level (1/2/3) :")))
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
            "generation_mode": 1
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


def ask_number(prompt, options, min_val, max_val):
    while True:
        try:
            text = prompt + " " + options + " : "
            value = int(input("{:45}".format(text)))

            if max_val == "inf" and min_val <= value:
                return value
            elif min_val <= value <= max_val:
                return value
            else:
                print(f"❌  Please enter a number between {min_val} and {max_val}!")
        except ValueError:
            print(f"❌  Please enter a valid number!")


def ask_yes_no(prompt):
    while True:
        text = prompt
        answer = input("{:45}".format(text)).lower()
        if answer in ('y', 'n'):
            return answer == 'y'
        else:
            print(f"❌  Enter only 'y' for yes or 'n' for no!")


def ask_print_file(prompt):
    while True:
        text = prompt
        answer = input("{:45}".format(text)).lower()
        if answer in ('print', 'file'):
            return answer
        else:
            print(f"❌  Enter only print or file!")

def print_default_settings_and_confirm(settings):
    print("-" * 80)
    print("{:^80}".format("📋  Default Settings Summary 📋"))
    print("-" * 80)
    print(f"{'Password length:':35} {settings.get('length', 12)}")
    print(f"{'Include lowercase:':35} {settings.get('use_lower', True)}")
    print(f"{'Include uppercase:':35} {settings.get('use_upper', True)}")
    print(f"{'Include digits:':35} {settings.get('use_digits', True)}")
    print(f"{'Include punctuation:':35} {settings.get('use_punct', True)}")
    print(f"{'Punctuation level:':35} {settings.get('punctuation_level', 1)}")
    print(f"{'Number of passwords:':35} {settings.get('num_passwords', 5)}")
    print(f"{'Output method:':35} {settings.get('output_method', 'print')}")
    print(f"{'Generation mode:':35} {settings.get('generation_mode', 1)}")

    answer = ask_yes_no(f"\n❓  Do you want to continue with these settings? (y/n): ")
    if not answer:
        print(f"\n👋  Exiting the program.")
        exit()



## Main Funcion

def generate_passwords():
    print_section(f"🔐  Password Generator  🔐")
    print_formatted(f"🤌  What would you like to do?")
    print_options("(1) Generate a new password")
    print_options("(2) Create a custom password" + "  WORK PROGRESS")
    print_options("(3) Use a default password")
    choice = ask_number(f"👉  Enter your choice","(1/2/3)",1,3)

    if choice == 1:
        print_section("🔧  Password Configuration  🔧")

        length = ask_number(f"🔢  Password length","(1-128)",1,128)
        use_lower = ask_yes_no("🔡  Include lowercase letters? (y/n) :")
        use_upper = ask_yes_no("🔠  Include uppercase letters? (y/n) :")
        use_digits = ask_yes_no("🔢  Include numbers? (y/n) :")
        use_punct = ask_yes_no("🔣  Include punctuation? (y/n) :")

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

        print_section(f"🛠️  Generation Options  🛠️")
        num_passwords = ask_number("🔢  How many passwords to generate? ","",1,"inf")
        output_method = ask_print_file("🖨️   Output method [print/file]: ")
        print_formatted(f"🎲  Generation mode:")
        print_options("(1) random")
        print_options("(2) sequential")
        generation_mode = ask_number(f"👉  Enter your choice","(1 or 2)",1,2)

    elif choice == 3:
        print_section("Using Default Settings")
        settings = load_default_settings()
        print_default_settings_and_confirm(settings)
        length = settings.get("length", 12)
        use_lower = settings.get("use_lower", True)
        use_upper = settings.get("use_upper", True)
        use_digits = settings.get("use_digits", True)
        use_punct = settings.get("use_punct", False)
        punctuation_level = settings.get("punctuation_level", 1)
        num_passwords = settings.get("num_passwords", 5)
        output_method = settings.get("output_method", "print")
        generation_mode = settings.get("generation_mode", 1)

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

    elif choice == 2:
        print_section("Custom Password")
        print("Custom password feature not yet implemented.")
        return
    else:
        print("Invalid option.")
        return

    passwords = []
    if generation_mode == 1:
        for _ in range(num_passwords):
            password = ''.join(secrets.choice(characters) for _ in range(length))
            passwords.append(password)
    elif generation_mode == 2:
        all_combinations = itertools.product(characters, repeat=length)
        for i, comb in enumerate(all_combinations):
            if i >= num_passwords:
                break
            passwords.append(''.join(comb))

    print_section(f"📝  Output  📝")
    if output_method == 'print':
        for pwd in passwords:
            print(pwd)
        print_formatted(f"\n✅  Successful generation!")

    elif output_method == 'file':
        file_name = str(input("{:45}".format("📋  Enter the filename : "))) + ".txt"
        with open(file_name, "w") as f:
            for pwd in passwords:
                f.write(pwd + "\n")
        print_formatted(f"✅  Successful generation! Passwords saved in the file: " + file_name)

# Main

if __name__ == "__main__":
    width = 80
    for line in logo.splitlines():
        print(line.center(width))
    check_or_create_default_file()
    generate_passwords()
