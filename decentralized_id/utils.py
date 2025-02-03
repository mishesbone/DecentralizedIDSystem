# decentralized_id/utils.py

import random
import string

def generate_verification_code(length=6):
    """Generate a random verification code consisting of digits and uppercase letters."""
    characters = string.ascii_uppercase + string.digits
    verification_code = ''.join(random.choice(characters) for _ in range(length))
    return verification_code
