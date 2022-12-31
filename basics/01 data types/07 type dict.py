
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
    print(a['a'])

if '222' in a:
    print(a['222'])

print('')
#change value of dict values
prices = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
for k, v in prices.items():
    prices[k] = round(v * 0.9, 2)  # Apply a 10% discount

print(prices)

print('')
#delete value of dict values
prices2 = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
for k, v in prices2.items():
    if k == 'orange':
        continue

print(prices2)

#Comprehensions
print('')

categories = ['color', 'fruit', 'pet']
objects = ['blue', 'apple', 'dog']
b_dict = {key: value for key, value in zip(categories, objects)}

print(b_dict) # {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}

print('\nTurning Keys Into Values and Vice Versa:')
#Turning Keys Into Values and Vice Versa

a_dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
print(a_dict) # {'one': 1, 'two': 2, 'thee': 3, 'four': 4}
new_dict = {value: key for key, value in a_dict.items()}
print(new_dict) # {1: 'one', 2: 'two', 3: 'thee', 4: 'four'}

print('')

#map()
prices3 = {'apple': 0.40, 'orange': 0.35, 'banana': 0.25}
def discount(current_price):
     return (current_price[0], round(current_price[1] * 0.95, 2))

new_prices = dict(map(discount, prices3.items()))
print(new_prices)