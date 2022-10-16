# iterowanie po tablicy
for v in [1,2,3,4]:
    print(v * 2)

# iterowanie po krotce
for v in ('Ania', 'Ola', 'Marta'):
    print(v)

# iterowanie po zbiorze
for el in {3,4,5,6,'Ola'}:
    print(el)  

# iterowanie po stringu
for v in 'Hello':
    print(v)
else:
    print('Pętla zakończona')

dict_data = {'Ania' : '1920', 'Patryk' : '720', 'Dawid' : 'brak'}

print('klucze #1')
# klucze #1
for keys in dict_data:
    print(keys)

print('klucze #2')
# klucze #2
for keys in dict_data.keys():
    print(keys)

print('wartości #1')
# wartości #1
for keys in dict_data.keys():
    print(dict_data[keys])

print('wartości #2')
# wartości #2
for values in dict_data.values():
    print(values)

# klucze i wartości
print('klucze i wartości')
for key, value in dict_data.items():
    print(key, ' : ', value)




