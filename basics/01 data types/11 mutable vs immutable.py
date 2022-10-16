
# immutable: int, float, bool, str, tuple, frozenset - niezmienne - operacje na nich utworzą nam nową wartość(obiekt)

a = 1
id_a_1 = id(a)

a += 1
id_a_2 = id(a)

print( id_a_1 )
print( id_a_2 )
print ( id(id_a_1) == id(id_a_2) )

# mutable: list, set, dict - zmienne - operacje są wykonywane na tym samym obiekcie
print(' ')

list_data = [1, 2, 3]
list_data_id_1 = id(list_data)

list_data += [4, 5, 6]
list_data_id_2 = id(list_data)

print(list_data_id_1)
print(list_data_id_2)
print( list_data_id_1 == list_data_id_2 )


