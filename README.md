<p align="center">
  <img src="https://github.com/user-attachments/assets/430461e5-2360-4ae5-b5c9-dc4a4190a964" alt="Pass Nasty in Stile Retro" width="500" />
</p>


**Nasty Pass** is an advanced, customizable password generator designed to create secure and unique passwords through a simple, guided terminal interface.

#### 🔐 Make Nasty Pass Your Go-To Tool Anytime!

To make Nasty Pass useful at any time of the day, I’ve created a lightweight demo you can use wherever you are — quick, simple, and always accessible.

👉 Try it here: [Nasty Pass Demo](https://sites.google.com/view/nastypass/nasty-password-generator)


## 📦 Features

- Generate random or sequential passwords
- Choose character sets: lowercase, uppercase, digits, punctuation
- Select punctuation level (basic to extended)
- Create custom passwords from your own words and numbers
- Generate letter-variant (leet-style) versions
- Save output to file or print to console
- Supports default settings via JSON

---

## 🚀 Getting Started

### 🔧 Requirements

- Python 3.7 or higher

### ▶️ Run the script

```bash
python3 nasty_pass.py
```

When run for the first time, the script creates a `default.json` file with the standard configuration.

---

## ⚙️ Usage Modes

### 1. **Random Password**
- Select length
- Choose which character types to include
- Specify number of passwords
- Choose output method (print or file)
- Select generation mode: random or sequential

### 2. **Custom Password**
- Input your own words/numbers
- Choose desired length
- Automatically generate all combinations
- Optional: create variants using letter substitutions (e.g., a → @, 4)
- Choose output method

### 3. **Use Default Settings**
- Load predefined configuration from `default.json`
- Skips prompts for faster use

---

## 🧠 Example

```text
================================================================================
                            🔐  Password Generator  🔐                            
================================================================================
🤌  What would you like to do?                                                   
    (1) Generate a new password
    (2) Create a custom password
    (3) Use a default password
👉  Enter your choice (1/2/3) :               1
================================================================================
                          🔧  Password Configuration  🔧                          
================================================================================
🔢  Password length (1-128) :                 14
🔡  Include lowercase letters? (y/n) :        y
🔠  Include uppercase letters? (y/n) :        n
🔢  Include numbers? (y/n) :                  y
🔣  Include punctuation? (y/n) :              n
================================================================================
                           🛠️  Generation Options  🛠️                           
================================================================================
🔢  How many passwords to generate?   :       1
🖨️   Output method [print/file]:             print
🎲  Generation mode:                                                             
    (1) random
    (2) sequential
👉  Enter your choice (1 or 2) :              1
================================================================================
                                  📝  Output  📝                                  
================================================================================
i77uapnr31fnxd

```

---

## 📁 Default Settings File

`default.json` is created automatically if not present. You can edit it to set your preferred defaults.

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

---

## 🔐 Security Notes

- Uses `secrets` module for cryptographic random generation
- Avoids use of dangerous functions (`eval`, `exec`, etc.)
- Input validation included for all interactive prompts
- Be cautious with long sequential generations: it may impact performance

---

## 📄 License

MIT License

---

## ✍️ Author

Developed by [emacarta](https://github.com/emacarta)


---

## 💋 Credits

Built with passion for those who want truly **nasty** passwords. 💀
