
contacts = {
    'a' : 'abc@gmail.com',
    "b" : 29,
    'c' : 'cad'
}

# dodwanie elementów do słownika
contacts['Rafał'] = 'rafal@gmail.com'

# odwoływanie się do słownika po kluczu -> wartość
print(contacts['a'])
print(contacts['b'])

if contacts['a'] in contacts:
    print('yes')
else:
    print('no')

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


a = {'a': '222', '222': 2}
if a['a'] in a:
    print('hello')

if '222' in a:
    print('hello222')