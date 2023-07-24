import random


def is_valid_password(password: str) -> bool:
    if len(password) < 8:
        return False
    
    if not any(char.isdigit() for char in password):
        return False
    
    if not any(char.islower() for char in password):
        return False
      
    if not any(char.isupper() for char in password):
        return False
     
    special_chars = {'+', '-', '*', '/', '!', '"', '№', ';', '%', ':', '?', '*', '(', ')', '='}
    if not any(char in special_chars for char in password):
        return False
    
    if ' ' in password:
        return False
    
    if not password.isascii():
        return False
    
    return True


def generate_random_number() -> int:
    return random.randint(0, 1000)
