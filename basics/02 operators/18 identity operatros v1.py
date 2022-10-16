
# operatory tożsamości

text = 'test' # obiekt

print( dir(text) )
print( text.capitalize() )
print( text.upper() )

number = 10 # obiekt
print( dir(number) )

a = [1,2,3,4,5]
b = a
c = b
d = c
e = [1,2,3,4,5]

print( a is b ) # True - to samo miejsce w pamięci
a.append(77)
b.append(88)
# te dwie zmienne są referencją do tego samego miejsca w pamięci
# te dwie zmienne wskazują na to samo miejsce w pamięci
print(a)
print(b)
print(d)

print(e)

# cały czas ten sam obiekt
print( a is not b ) # False

# inna lista, inna obiekt
print( a is e ) # False
print( a is not e ) # True





