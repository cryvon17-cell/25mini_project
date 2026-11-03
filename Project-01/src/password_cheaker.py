# Password Strength Checker
# Project 01

from getpass import getpass

# Take password input from user
password = getpass("Enter your password: ")

# Calculate password length
length = len(password)

# Check password length
if length < 8:
    print("Password Strength: WEAK")
    print("Your password must contain at least 8 characters.")

else:
    print("Password Strength: GOOD")
    print("Your password has at least 8 characters.")
# Password Strength Checker
# Project 01 - Version 2

from getpass import getpass

# Take password input
password = getpass("Enter your password: ")

# Check password length
length = len(password)

# Check security criteria
has_uppercase = any(char.isupper() for char in password)

has_lowercase = any(char.islower() for char in password)

has_number = any(char.isdigit() for char in password)

has_special = any(
    not char.isalnum() and not char.isspace()
    for char in password
)

# Calculate score
score = 0

if length >= 12:
    score += 1

if has_uppercase:
    score += 1

if has_lowercase:
    score += 1

if has_number:
    score += 1

if has_special:
    score += 1

# Display results
print("\n--- PASSWORD SECURITY REPORT ---")

print("Password Length:", length)
print("Uppercase:", has_uppercase)
print("Lowercase:", has_lowercase)
print("Number:", has_number)
print("Special Character:", has_special)

print("Security Score:", score, "/ 5")

if score <= 2:
    print("Password Strength: WEAK")

elif score <= 4:
    print("Password Strength: MEDIUM")

else:
    print("Password Strength: STRONG")
