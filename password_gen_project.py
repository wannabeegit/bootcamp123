# PASSWORD GENERATOR

import random
import string
chars = string.ascii_letters+string.digits+string.punctuation
print(random.choice(chars))
#length = 12
length = int(input('password length: '))
password = ''

for _ in range(length):
    x = random.choice(chars)
    password += x
print(f'your password is: {password}')