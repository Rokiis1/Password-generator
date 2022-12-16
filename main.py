import secrets
import random
import string

def generate_password(length, letters=True, digits=True, punctuation=True):
    """Generate a secure random password with the given length"""
    # Start with an empty list of characters
    characters = []

    # Add letters to the list if specified
    if letters:
        characters += string.ascii_letters

    # Add digits to the list if specified
    if digits:
        characters += string.digits

    # Add punctuation to the list if specified
    if punctuation:
        characters += string.punctuation

    # Shuffle the list of characters to get a random order
    random.shuffle(characters)
    # Select the first `length` characters from the shuffled list
    password = ''.join(characters[:length])
    return password

# Generate a password with 10 characters, including letters and digits
password = generate_password(10, letters=True, digits=True, punctuation=False)
print(password)

# Generate a password with 15 characters, including letters, digits, and punctuation
password = generate_password(15, letters=True, digits=True, punctuation=True)
print(password)