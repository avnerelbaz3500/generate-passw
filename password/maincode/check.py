
import re


from .create import Create

def calculate_password_strength(password):
    score = 0
    length = len(password)

    knownpass = Create.knownpassw(2)

    # Check length
    if password == None:
        strength = {'percent': 0, 'message': '', 'colorClass': 'bg-dark'}
        return strength
    if length >= 8:
        score += 1
    if length >= 12:
        score += 1
    if length >= 14:
        score += 1
    if length >= 16:
        score += 1



    # Check for different character types
    if re.search(r'[a-z]', password):
        score += 1  # Lowercase
    if re.search(r'[A-Z]', password):
        score += 1  # Uppercase
    if re.search(r'[0-9]', password):
        score += 1  # Digits
    if re.search(r'[\W_]', password):
        score += 1  # Special characters

    # Determine strength
    
    if password in knownpass:
        strength = {'percent': 100, 'message': 'Pwned', 'colorClass': 'bg-dark'}
    elif score <= 4 :
        strength = {'percent': (score / 8) * 100, 'message': 'Weak', 'colorClass': 'bg-danger'}
    elif score <= 6:
        strength = {'percent': (score / 8) * 100, 'message': 'Moderate', 'colorClass': 'bg-warning'}
    elif score <= 7:
        strength = {'percent': (score / 8) * 100, 'message': 'Strong', 'colorClass': 'bg-info'}
    else:
        strength = {'percent': (score / 8) * 100, 'message': 'Very Strong', 'colorClass': 'bg-success'}

    return strength

