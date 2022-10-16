
list_1 = ['Ala', 'Ola', 'Kasia']
print(list_1)

list_1[0] = 'Patryk'
print(list_1)

names_list = list_1 + ['Agnieszka']
print(names_list)
print(len(names_list))
print(type(names_list ))

empty_list = []
print(empty_list)

# odwoływanie się po indeksie
print(list_1[0])
print(names_list[-1])
print(names_list[1:3])

# lista wielopoziomowa
cars = [ ['honda', 'maserati'], ['matiz', 'kia'] ]
print(cars[1][1])

if 'honda' in cars[0]: # True - wykona
    print('honda w krotce pierwszej')

if 'honda' in cars[1]: # False - niewykona
    print('honda w krotce pierwszej')

# usuwanie listy
del list_1

# usuwanie elementu listy
print(names_list)
del names_list[0]
print(names_list)

# dodawanie elementów list do siebie
list_3 = [1, 2, 3]
list_4 = [4, 5, 6]

numbers_list = list_3 + list_4
print(numbers_list )

# mnożenie elementów list
numbers_list_x_2 = numbers_list * 2
print(numbers_list_x_2)