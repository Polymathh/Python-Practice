import string
password = input("Enter your password: ")

length = len(password) >= 8
has_digit = any(char.isdigit() for char in password)
has_symbol = any(char in string.punctuation for char in password)

if length and has_digit and has_symbol:
    print("✅ Strong password")
else:
    print("❌ Weak password. Use 8+ chars, numbers, and symbols.")