
smallest = None
print('Before')
digits = [9, 41, 12, 3, 74, 15]
for value in digits:
    if smallest is None:
        smallest = value
    elif value < smallest:
        smallest = value
    print(smallest, value)
print('After', smallest)

print(min(digits))
