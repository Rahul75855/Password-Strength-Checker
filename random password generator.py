# random password generator
import random
import string

def check_password(password):
  score = 0
  if len(password) >= 8:
    score += 1
  if any(c.isupper() for c in password):
    score += 1
  if any(c.islower() for c in password):
    score += 1
  if any(c.isdigit() for c in password):
    score += 1
  if any(not c.isalnum() for c in password):
    score += 1

  if score <= 2:
    return "Weak"
  elif score <= 4:
    return "Medium"
  else:
    return "Strong"


def generate_strong_password(length=12):
  # All kinds of characters are defined.
  lower = string.ascii_lowercase  # a-z
  upper = string.ascii_uppercase  # A-Z
  digits = string.digits  # 0-9
  symbols = string.punctuation  # @, #, $, %, etc.

  # Ensure that the password has at least one uppercase, lowercase, digit, and symbol
  password = [
      random.choice(lower),
      random.choice(upper),
      random.choice(digits),
      random.choice(symbols),
  ]

  # Will add random characters for the rest of the length (default 12 total)
  all_chars = lower + upper + digits + symbols
  for _ in range(length - 4):
    password.append(random.choice(all_chars))

  # Shuffle the list so that the pattern is not predictable
  random.shuffle(password)

  # convert list to string and return.
  return "".join(password)


# Main Program
password = input("Enter password to check strength: ")
strength = check_password(password)
print("Password Strength:", strength)

# If password is weak or medium ,suggest a recommended password.
if strength != "Strong":
  print("\n⚠️ Your password is weak!")
  print("Recommended Strong Password:", generate_strong_password())
