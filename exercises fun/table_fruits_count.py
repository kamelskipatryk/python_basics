fruits = ["apple", "banana", "cherry", "apple", "apple", "apple", "apple", "banana", "cherry"]
cApple = 0
cBanana = 0
cCherry = 0
for fruit in fruits:
    if fruit == 'apple':
        cApple += 1
    if fruit == 'banana':
        cBanana += 1
    if fruit == 'cherry':
        cCherry += 1

print(f'Apple: {cApple}, Banana: {cBanana}, Cherry: {cCherry}')