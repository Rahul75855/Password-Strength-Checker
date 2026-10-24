# Password-Strength-Checker

# Secure Password Strength Checker & Generator

A lightweight and efficient Python-based tool designed to evaluate user password security and automatically generate strong, randomized passwords to enhance digital safety.

---

## Features

* **Real-time Strength Analysis:** Evaluates passwords based on 5 crucial security criteria:
  * Minimum length of 8 characters.
  * Presence of uppercase letters (`A-Z`).
  * Presence of lowercase letters (`a-z`).
  * Inclusion of numeric digits (`0-9`).
  * Inclusion of special symbols (`@`, `#`, `$`, `!`, etc.).
* **Smart Categorization:** Classifies passwords into **Weak**, **Medium**, and **Strong**.
* **Automatic Password Generator:** If a password is evaluated as *Weak* or *Medium*, the script automatically generates a highly secure 12-character randomized password mixing uppercase, lowercase, numbers, and symbols.

---

## Technologies Used

* **Language:** Python 3.x
* **Built-in Libraries:** 
  * `random` (for generating random selections)
  * `string` (for character sets management)

---

## How to Run the Project

1. Make sure you have Python installed on your system.
2. Clone this repository or download the script file (`password_checker.py`).
3. Open your terminal or command prompt and run the script:
   ```bash
   python password_checker.py
