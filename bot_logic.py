import random
import string

def gen_pass(length):
    
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''

    for _ in range(length):
        password += random.choice(characters)

    return password
