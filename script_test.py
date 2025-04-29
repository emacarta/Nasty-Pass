import itertools
import random

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

def get_inputs():
    elements = input("Enter words or numbers separated by spaces: ").split()
    elements = [e.lower() for e in elements]
    total_chars = sum(len(e) for e in elements)
    print(f"Total number of characters in the entered elements: {total_chars}")
    password_length = int(input("Desired password length: "))
    return elements, password_length

def generate_variants(elements, password_length):
    words = [e for e in elements if not e.isdigit()]
    numbers = [e for e in elements if e.isdigit()]

    total_chars = sum(len(w) for w in words) + sum(len(n) for n in numbers)
    reduce_by = total_chars - password_length

    if reduce_by <= 0:
        word_variants = [[w] for w in words]
    else:
        word_variants = []
        for word in words:
            cuts = []
            min_len = 1 if len(word) > 1 else len(word)
            for i in range(min_len, len(word)+1):
                cuts.append(word[:i])
            word_variants.append(cuts)

    number_variants = [[n] for n in numbers]
    all_elements = word_variants + number_variants

    all_combinations = []
    for subset in itertools.permutations(all_elements):
        for variant in itertools.product(*subset):
            candidate = ''.join(variant)
            if len(candidate) == password_length:
                all_combinations.append(candidate)

    return list(set(all_combinations))

def generate_letter_variants(password):
    variants = ['']
    for char in password:
        lower_char = char.lower()
        if lower_char in letter_variants:
            new_variants = []
            for variant in variants:
                for replacement in [char] + letter_variants[lower_char]:
                    new_variants.append(variant + replacement)
            variants = new_variants
        else:
            variants = [v + char for v in variants]
    return variants

def main():
    elements, password_length = get_inputs()
    all_passwords = generate_variants(elements, password_length)

    print(f"\nTotal number of possible combinations: {len(all_passwords)}")

    if not all_passwords:
        print("No possible combination with the given restrictions.")
        return

    number_of_passwords = int(input("How many passwords do you want to generate?: "))
    mode = input("Do you want random (r) or sequential (s) generation? (r/s): ").strip().lower()

    if mode == 'r':
        selected = random.sample(all_passwords, min(number_of_passwords, len(all_passwords)))
    else:
        selected = all_passwords[:number_of_passwords]

    print("\nGenerated passwords:")
    for pwd in selected:
        print(pwd)

    variant_choice = input("Do you want to generate variants of the passwords using alternative letters? (y/n): ").strip().lower()
    if variant_choice == 'y':
        print("\nPassword variants:")
        for pwd in selected:
            variants = generate_letter_variants(pwd)
            for v in variants:
                print(v)

if __name__ == "__main__":
    main()
