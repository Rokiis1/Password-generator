import secrets
import string

def generate_password(length):
    """Generate a secure random password with the given length"""
    # Get a list of all the ASCII characters
    characters = string.ascii_letters + string.digits + string.punctuation
    # Generate a secure random password using the secrets module
    password = ''.join(secrets.choice(characters) for i in range(length))
    return password

# Generate a password with 20 characters
password = generate_password(20)
print(password)