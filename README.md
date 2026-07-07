# Number-System-Converter
![Status](https://img.shields.io/badge/Status-Work%20in%20Progress-orange)

A lightweight CLI tool to convert numbers between different numeral systems (Decimal, Binary, etc.). It works both as an interactive menu and via direct terminal arguments.

---

## 🚀 Features

- **Dual Mode:** Use the interactive menu or pass arguments to convert instantly.
- **Built-in Help:** Clean interface documentation using standard `--help`.
- **Modular Code:** Separated logic, menu handling, and entry point for easy scaling.
---

- Decimal -> Binary
- Decimal -> Hexadecimal
- Binary -> Decimal
- Binary -> Hexadecimal
- Hexadecimal -> Decimal
- Hexadecimal -> Binary 

---

## 🛠️ Installation & Setup

### Prerequisites
Make sure you have **Python 3.x** installed.

### Global Installation via Pip
You can install the tool directly from PyPI:

```bash
pip install simple-number-converter
```
### Running the programm
```bash
# Option 1: Start the interactive menu
numconv

# Option 2: Convert instantly using arguments
numconv --dectobin 42
numconv -db 42
```
### 2. Running option
```bash
# Option 1: Start the interactive menu
python main.py

# Option 2: Convert instantly using arguments
python main.py --dectobin 42
python main.py -db 42