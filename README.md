<p align="center">
  <img src="https://github.com/user-attachments/assets/430461e5-2360-4ae5-b5c9-dc4a4190a964" alt="Pass Nasty in Stile Retro" width="500" />
</p>


**Nasty Pass** is an advanced, customizable password generator designed to create secure and unique passwords through a simple, guided terminal interface.

⚠️ **WARNING**: This code is currently in beta. ⚠️

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

## 🧠 Examples

```text
...
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
