import random

def make_password(length):
    symbols = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"

    password = ""
    for i in range(length):
        password += random.choice(symbols)

    return password

print(make_password(10))
