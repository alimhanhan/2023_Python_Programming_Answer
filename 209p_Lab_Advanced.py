import random

def make_passwords():
    alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = "0123456789"
    password = ""

    for i in range(3):
        index1 = random.randrange(len(alphabet))
        index2 = random.randrange(len(number))
        password = password + alphabet[index1] + number[index2]

    return password

print('새롭게 생성된 패스워드:', make_passwords())