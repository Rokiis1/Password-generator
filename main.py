import bcrypt
import secrets
import string

def generate_password(length):
    # Define the character set to use for the password
    characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase

    # Generate a random string using the character set
    password = ''.join(secrets.choice(characters) for _ in range(length))

    # Make sure the password includes at least one uppercase letter, one lowercase letter, and one digit
    if not any(c.islower() for c in password):
        password = secrets.choice(string.ascii_lowercase) + password[1:]
    if not any(c.isupper() for c in password):
        password = secrets.choice(string.ascii_uppercase) + password[1:]
    if not any(c.isdigit() for c in password):
        password = secrets.choice(string.digits) + password[1:]
    
    # Ensure that the password includes at least one uppercase and one lowercase letter
    if not any(c.islower() for c in password) or not any(c.isupper() for c in password):
        password = secrets.choice(string.ascii_lowercase) + secrets.choice(string.ascii_uppercase) + password[2:]

    return password

def hash_password(password):
    # Hash the password using bcrypt
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
    return hashed_password

def verify_password(password, hashed_password):
    # Check if the password matches the hashed password
    if bcrypt.checkpw(password.encode('utf-8'), hashed_password):
        return True
    else:
        return False

# Generate a password
password = generate_password(16)
print(f"Generated password: {password}")

# Hash the password
hashed_password = hash_password(password)
print(f"Hashed password: {hashed_password}")

# Verify the password
if verify_password(password, hashed_password):
    print("Password is valid")
else:
    print("Password is invalid")




