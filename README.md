# Nasty Pass

**Nasty Pass** is an advanced, customizable password generator designed to create secure and unique passwords through a simple, guided terminal interface.

---

## ✨ Main Features

- Random password generation with custom settings
- Use of lowercase, uppercase letters, digits, and symbols
- Three selectable punctuation levels
- Random or sequential generation modes
- Save passwords to a file or print to terminal
- Quick generation using default settings
- Automatically creates a `default.json` settings file
- Leet-style character variations (work in progress)

---

## 📦 Python Libraries Used

- `random`
- `secrets`
- `itertools`
- `textwrap`
- `json`
- `os`

---

## 🚀 How to Use

1. **Installation**  
   No special installation required. Just use Python 3.

2. **Run**  
   Launch the program:
   ```bash
   python nasty_pass.py
   ```

3. **Initial Choices**  
   Choose between:
   - Generating a new custom password
   - (In development) Creating a custom-designed password
   - Using default settings

4. **Configuration**  
   When generating a new password, you can set:
   - Password length
   - Types of characters to include (lowercase, uppercase, digits, punctuation)
   - Punctuation level (1 = basic, 2 = intermediate, 3 = extended)
   - Number of passwords to generate
   - Output method (`print` or `file`)
   - Generation mode (`random` or `sequential`)

5. **Output**  
   View passwords directly in the terminal or save them into a `.txt` file.

---

## 🛠️ Configuration File (`default.json`)

At first run, a `default.json` file is automatically created with these settings:

```json
{
    "length": 12,
    "use_lower": true,
    "use_upper": true,
    "use_digits": true,
    "use_punct": true,
    "punctuation_level": 2,
    "num_passwords": 5,
    "output_method": "print",
    "generation_mode": 1
}
```

You can manually edit this file to change the default behavior.

---

## ⚡ To-Do and Future Improvements

- Implement the "Custom Password" feature
- Fix visualization for punctuation level 3
- Add automatic leet-style transformations
- Support multiple configuration profiles
- Enable batch mode for high-volume password generation

---

## 💋 Credits

Built with passion for those who want truly **nasty** passwords. 💀
