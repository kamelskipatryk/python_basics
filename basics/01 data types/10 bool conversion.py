
# false
print( bool() ) # brak przekazanej wartości zwróci domyślnie False
print( bool(False) ) # False
print( bool(0) ) # False
print( bool(0.0) ) # False
print( bool( () ) ) # puste krotki dają False
print( bool( [] ) ) # puste listy dają False
print( bool( {} ) ) # puste zbiory dają False
print( bool('') ) # pusty łańuch znaków daje False
print( bool(None) ) # None - brak przypisanej wartości - False

# true
print( bool(True) ) # True
print( bool(1) ) # True
print( bool(5) ) # True
print( bool(-10) ) # True
print( bool( ('ola', 1) ) ) # krotka z przynajmniej jednym elementem == True
print( bool( [0] ) ) # lista z przynajmniej jednym elementem == True
print( bool( {0} ) ) # zbiory z przynajmniej jednym elementem == True
print( bool('x') ) # string z przynajmniej jednym znakiem == True