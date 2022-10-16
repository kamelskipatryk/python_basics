
data = { 'name' : 'Ola', 'city' : 'Waw' }

# pobranie wartości danego klucza
print( data['name'])

# zdefiniowanie klucza
#data_postal_code = 'postal_code' - klucz do zmiennej
# dodanie nowego klucza do istniejącego słownika o wartości 12345
data['postal_code'] = 12345

print(data) # {'name': 'Ola', 'city': 'Waw', 'postal_code': 12345}

# len -> długość słownika, tzn. ile jest kluczy
print(len(data)) # 3

# del -> kasowanie klucza oraz wartości
del data['city']
print(data) # {'name': 'Ola', 'postal_code': 12345}

# clear -> kasowanie wszystkich elementów
data.clear()
print(data) # {}, pusty słównik

data = { 'name': 'Klaudia', 'city': 'Ino' }
# copy -> tworzenie płytkiej kopii, po skopiowaniu tworzy referencje a nie nowy element
data_copy = data.copy()
print(data_copy) # {'name': 'Klaudia', 'city': 'Ino'}
print( data['name'] is data_copy['name'] ) # True, to jest referencja do tego samego obiektu
print( data is data_copy ) # False, słowniki jako inne obiekty, elementy w środku te same

# dict.fromkeys -> tworzenie nowego słownika, nowego obiektu i nowych elementów
data_copy_2 = dict.fromkeys(('name', 'city', 'code')) # bez drugieo argumentu daje wartości None
print(data_copy_2) # {'name': None, 'city': None, 'code': None}

data_copy_3 = dict.fromkeys(('name', 'city', 'code'), 0) # podany drugi argument 0
print(data_copy_3) # {'name': 0, 'city': 0, 'code': 0}

# get -> odwołanie się do klucza, którego nie ma -> zwrócona wartość default
print( data_copy_2.get('klucz_nie_ma', 'default') )

# czy klucz istnieje w słowniku
print( 'name' in data_copy_2 ) # True

# keys -> fukncja do uzyskania listy kluczy
print( data_copy_2.keys() ) # dict_keys(['name', 'city', 'code'])

# values -> fukncja do uzyskania listy wartości
print( data_copy_2.values() ) # dict_values([None, None, None])
