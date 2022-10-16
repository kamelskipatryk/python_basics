
num = 0
operation = None
reset = True
result = None
calc_operations = ['+','-','*','/','**']

while True:
    if reset == True:
        num =  input('Podaj liczbę startową: ')
        if num.isnumeric():
            num = int(num)
        else:
            continue
        reset = False

    operation = input('Podaj operację arytmetyczną jedną z ' + str(calc_operations) + ', reset lub exit: ')
    if operation == 'exit': break
    if operation == 'reset':
        reset = True
        continue

    if not operation in calc_operations:
        print('Podano nieznaną komendę!')
        continue

    while True:
        second_num = input('Podaj drugą liczbę: ')
        if second_num.isnumeric():
            second_num = int(second_num)
            break
        else:
            continue

    if operation == '+':
        result = num + second_num

    if operation == '-':
        result = num - second_num

    if operation == '*':
        result = num * second_num

    if operation == '/':
        result = num / second_num

    if operation == '**':
        result = num ** second_num

    print(f'Wynik operacji: {str(num)} {operation} {str(second_num)} = {str(result)}')
    num = result
    result = None

