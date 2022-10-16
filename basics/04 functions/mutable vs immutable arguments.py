
# immutable: int, float, bool, str, frozenset
# próba modyfikacji sprawi utworzenie nowego obiektu o nowym id

def modify_str(string_data):
    print(id(string_data))
    string_data += '!'
    print(id(string_data))
    print(string_data)

string = 'Hello'

modify_str(string)
print(string) # Hello
print('')
# mutable: list, set, dict
# próba modyfikacji zmieni daną zmienną bez tworzenia nowego obiektu, zostaje to samo id

# ta sama lista
print('ta sama lista')

def modify_list(list_data):
    print( id(list_data))
    list_data.append(10)
    print( id(list_data))
    print(list_data)

list_value = [0,1,2]
print( id(list_value))
modify_list(list_value)
print('')

# nowa lista we funkcji - nowy obiekt lista
print('nowa lista')

def modify_list_2(list_data):
    print( id(list_data)) # 2309460964224
    print(list_data) # [9, 8, 7]
    list_data = [1,2,3,4,5,6,7] # osobna lista, nowy obiekt
    list_data.append(10)
    print( id(list_data)) # 2309460964160
    print(list_data) # [1, 2, 3, 4, 5, 6, 7, 10]

list_value_2 = [9,8,7]
print('pierwsze')
print( id(list_value_2)) # 2309460964224
modify_list_2(list_value_2)










