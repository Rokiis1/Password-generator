import secrets
import string

def generate_password(length):
    # Define the character set to use for the password
    characters = string.ascii_letters + string.digits + string.punctuation + string.ascii_uppercase + string.ascii_lowercase

    # Generate a random string using the character set
    password = ''.join(secrets.choice(characters) for i in range(length))

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

# Generate a password
password = generate_password(16)
print(password)




