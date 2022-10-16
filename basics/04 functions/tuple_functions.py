
# + -> konkatenacja, łączenie krotek -> dodawanie krotek
tuple_1 = (0,1) + (2,3) + (4,)
print(tuple_1) # (0, 1, 2, 3, 4)

# * -> powtórzenie list
print( (1,2) * 3 ) # (1, 2, 1, 2, 1, 2)

# in -> sprawdzenie czy dany element znajduje się w krotce
print( 3 in tuple_1 ) # True

# not in -> sprawdzenie czy dany element nie znajduje się w krotce
print( 3 not in tuple_1 ) # False

# len -> długość krotki
print( len(tuple_1) ) # 5

# pobranie elementu o indeksie 4
print( tuple_1[4] ) # 4

# pobranie zakresu
print( tuple_1[1:3] ) # (1, 2)

# zmiana elementu krotki jest niemożliwa
# tuple_1[2] = 8 # błąd

# usunięcie elementu krotki jest niemożliwe
# del tuple_1[2] # błąd

# iterowanie po krotce
for number in tuple_1:
    print(number)

# max -> maksymalna/największa wartość w krotce
print( max(tuple_1) ) # 4

# min -> minimalna/najmniejsza wartość w krotce
print( min(tuple_1) ) # 0

# tuple -> zamiana listy na krotkę
print( list( tuple_1 ) ) # [0, 1, 2, 3, 4]