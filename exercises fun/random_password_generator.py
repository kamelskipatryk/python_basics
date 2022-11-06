import random

lower = 'qwertyuiopasdfghjklzxcvbnm'
upper = lower.upper()
symbols = '`!@#$%^&*()_+-={]{]:;<>,./\?'
numbers = '1234567890'

all = lower + upper + symbols + numbers

length = 15

password = ''
for _ in range(length):
    password = ''.join([password,random.choice(all)])

print(password)



