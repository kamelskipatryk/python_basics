
number = 5

while number > 0:
    print(number)
    number -= 1

print(' ')

number = 1

while number < 6:
    print(number)
    number += 1

num = 0
while True:
    print('Wprowadź liczbę lub exit, aby zakończyć program.')
    str_data = input()
    if str_data == 'exit': break
    num += int(str_data)
    print('Wartość po dodaniu', str(str_data),'wynosi', str(num))

num_2 = 3

while num_2 > 0:
    print(num_2)
    num_2 -= 1
    if num_2 == 10: break
else:
    print('Num_2 wynosi: ' + str(num_2))





