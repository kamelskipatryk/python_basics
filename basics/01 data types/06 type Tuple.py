
tuple_1 = ('Ala', 'Ola', 'Kasia')
print(tuple_1)

# tuple_1[0] = 'Patryk' # błąd! - tupla jest niemutowalna/niezmienialna

# names_tuple = tuple_1 + ('Patryk') - TypeError: can only concatenate tuple (not "str") to tuple

names_tuple = tuple_1 + ('Patryk', )
print(names_tuple)
print(len(names_tuple))
print(type(names_tuple))

tuple_2 = 1 ,2 ,3 # tuple_2 = 1 ,2 ,3 == tuple_2 = (1 ,2 ,3)
print(tuple_2)

empty_tuple = ()
print(empty_tuple)

# odwoływanie się po indeksie
print(names_tuple[0])
print(names_tuple[-1])
print(names_tuple[1:3])

# krotka wielopoziomowa
cars = ( ('porshe', 'ford') , ('mercedes', 'kia') )
print(cars[0][1])

if 'ford' in cars[0]: # True - wykona
    print('ford w krotce pierwszej')

if 'ford' in cars[1]: # False - nie wykona
    print('ford w krotce pierwszej')

# usuwanie krotki
del empty_tuple

# usuwanie elementu w krotce - nie można!
# del names_tuple[0]

cars_x_2 = cars * 2
print(cars_x_2)






