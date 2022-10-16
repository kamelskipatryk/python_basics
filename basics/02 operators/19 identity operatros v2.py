# referencja działa wstecz - ten sam obiekt
a = [1,2,3,4,5]
b = a
b.append(99)
print(a) # [1, 2, 3, 4, 5, 99]
print(b) # [1, 2, 3, 4, 5, 99]
print( a is b ) # True

# stworzenie nowej listy, stworzenie nowego obiektu
c = [1,2,3,4,5]
d = [1,2,3,4,5]
d.append(99)
print(c) # [1, 2, 3, 4, 5]
print(d) # [1, 2, 3, 4, 5, 99]
print( c is d ) # False
