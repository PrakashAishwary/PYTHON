import re

def check_password_strength(password):
    """
    Validate the strength of a password.
    Returns a message if the password is strong or weak.
    """

    # Minimum 8 characters
    if len(password) < 8:
        return "Password too short (minimum 8 characters)."
    
        # At least one lowercase letter
    if not re.search(r"[a-z]", password):
        return "Password must contain at least one lowercase letter."

    # At least one uppercase letter
    if not re.search(r"[A-Z]", password):
        return "Password must contain at least one uppercase letter."

    # At least one digit
    if not re.search(r"\d", password):
        return "Password must contain at least one digit."

    # At least one special character
    if not re.search(r"[!@#$%^&*()_+=\-{}\[\]:;\"'<>,.?/~`|\\]", password):
        return "Password must contain at least one special character."

    return "Detected strong password!!!"

# Test it
while True:
    pwd = input("Enter a password to check (or 'q' to quit): ")
    if pwd.lower() == 'q':
        break
    result = check_password_strength(pwd)
    print(result)