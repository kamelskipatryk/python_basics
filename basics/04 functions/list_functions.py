list_1 = [0,1,2,3,4,5]

# pobranie elementu o indeksie 0
print( list_1[0] ) # 0

# pobranie zakresu
print( list_1[2:5] ) # [2, 3, 4]

list_2 = ['Ala','Damian','Patryk','Radek',]
# zmiana elementu
list_2[2] = 'Igor'
print( list_2 ) # Igor zamiast Patryk -> ['Ala', 'Damian', 'Igor', 'Radek']

# del -> kasowanie elementu
del list_2[0]
print(list_2) # ['Damian', 'Igor', 'Radek']

# len -> długość listy
print( len(list_2) ) # 3

# max -> największa wartość w liście
print( max([0,1,5,3,4]) ) # 5
print( max(list_2) ) # jeżeli stringi to najwyższy indeks -> Radek

# min -> najmniejsza wartość w liście
print( min([0,1,5,3,4]) ) # 0

# list -> zamiana krotki na listę
print( list( (5,10) ) ) # [5, 10]

# + -> łączenie list
print( [0,1] + [2,3] ) # [0, 1, 2, 3]

# * -> powtórzenie list
print( [0,1] * 2 ) # [0, 1, 0, 1]

# in -> sprawdzenie czy element listy znajduje się w danej liście
print( 5 in [3,4,5] ) # True
print( 'Patryk' in ['Patryk',4,5] ) # True

# not in -> sprawdzenie czy element listy nie znajduje się w danej liście
print( 5 not in [3,4,5] ) # False
print( 'Ola' not in ['Patryk',4,5] ) # True

# iterowanie po liście
list_of_capitals_names = ['Warszawa', 'Berlin', 'Londyn']

for capital_name in list_of_capitals_names:
    print(capital_name)

# append -> dodawanie nowego elementu do listy
list_of_capitals_names.append('Warszawa')
print(list_of_capitals_names) # ['Warszawa', 'Berlin', 'Londyn', 'Warszawa']

# count -> ilość powtórzeń elementu listy
print( list_of_capitals_names.count('Warszawa') ) # 2

# extend -> rozszerzenie listy o nowe elementy z innej sekwencji
# dodanie elementów do listy z innej sekwencji
list_of_capitals_names.extend( ('Paryż', 'Oslo') )
print( list_of_capitals_names ) # ['Warszawa', 'Berlin', 'Londyn', 'Warszawa', 'Paryż', 'Oslo']

# index -> zwraca najmniejszy index(pierwszy z lewej) wystąpienia wybranej wartości
print( list_of_capitals_names.index('Warszawa') ) # 0

# insert -> umieszczenie elementu pod wskazanym indeksem, przesuwa istniejący dalej
list_of_capitals_names.insert(0, 'Barcelona')
print(list_of_capitals_names) # ['Barcelona', 'Warszawa', 'Berlin', 'Londyn', 'Warszawa', 'Paryż', 'Oslo']

list_of_numbers = [1,65,43,23,7]
# reverse -> odwrócenie kolejności
list_of_numbers.reverse()
print(list_of_numbers) # [7, 23, 43, 65, 1]

# sort -> sortowanie od najmniejszej wartości do największej
list_of_numbers.sort()
print( list_of_numbers ) # [1, 7, 23, 43, 65]

# pop -> zwraca i zabiera/usuwa ostatni element z listy
print( list_of_numbers.pop() ) # 65
print(list_of_numbers) # [1, 7, 23, 43]




