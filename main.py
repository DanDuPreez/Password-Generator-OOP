import random

# Function to generate a random password
def generate_password(length):
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()"
    password = ''.join(random.choice(characters) for i in range(length))
    return password

# Function to check password strength
def check_password_strength(password):
    # Define criteria for a strong password
    criteria = {
        'length': len(password) >= 8,
        'lowercase': any(char.islower() for char in password),
        'uppercase': any(char.isupper() for char in password),
        'digit': any(char.isdigit() for char in password),
        'special': any(char in "!@#$%^&*()" for char in password)
    }
    # Count how many criteria are met
    strength = sum(criteria.values())
    return strength

# Generate and print a random password of length 12
password = generate_password(12)
print("Generated password:", password)

# Check the strength of the generated password
strength = check_password_strength(password)
print("Password strength:", strength)