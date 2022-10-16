
float_num = 23.78884
int_num = int(float_num)

print(type(int_num))
print(int_num)

print(int(' 23455   '))

int_num = 56
float_num_2 = float(int_num)
print(float_num_2)

text = '123.3463456'
float_num_2 = float(text)
print(float_num_2)

print('Wartość float_num_2: ' + str(float_num_2) + ' ' + str(98) + ' ' + str([1, 2, 3, 4]))
print('Wartość float_num_2: ', float_num_2, 89, [5, 6, 7, 8])

# konwersja listy na krotke
list_data = [1, 2, 3, 4]

tuple_data = tuple(list_data)
print(tuple_data)

# konwersja krotki na liste
tuple_data_2 = (1, 2, 'ola')

list_data_2 = list(tuple_data_2)
print(list_data_2)