list_1 = [2, 4, 6]

number = int(input('Podaj liczbę: '))

if number > sum(list_1):
    print(f'Liczba: {number}, jest większa od sumy liczb w liście.')
elif number < sum(list_1):
    print(f'Liczba: {number}, jest mniejsza od sumy liczb w liście.')
else:
    print(f'Liczba: {number}, jest równa sumie liczb w liście.')

num = [2, 3, 4, 5]
print()
print(all(x > 1 for x in num))
print(all(x > 4 for x in num))
print()






