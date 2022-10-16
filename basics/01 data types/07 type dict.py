
contacts = {
    'Patryk' : 'patryk@gmail.com',
    "Ola" : 29,
    'Paweł' : 'elektryk'
}

# dodwanie elementów do słownika
contacts['Rafał'] = 'rafal@gmail.com'

# odwoływanie się do słownika po kluczu -> wartość
print(contacts['Ola'])
print(contacts['Patryk'])

print(type(contacts))
print(len(contacts))

# wyświetlenie kluczy ze słownika
print(contacts.keys())

# wyświetlenie wartości ze słownika
print(contacts.values())

# iterowanie po elemntach słownika
for k in contacts:
    print( k + ' ' + str(contacts[k]))

print(' ')

for key, value in contacts.items():
    print( key + ' ' + str(value))