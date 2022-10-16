
print( 'Hello' + 'World!' ) # HelloWorld! -> powstanie nowy string, bo str jest niemutowalny
print( 'Hello' * 3) # HelloHelloHello

welcome_text = 'Hello World!'
print( welcome_text[0] ) # H
print( welcome_text[0:5] ) # Hello

print( 'Hello' in welcome_text ) # True
print( 'Hello' not in welcome_text ) # False

multiline = '''line_1
line_2
line_3'''

print(multiline)
# line_1
# line_2
# line_3

# capitalize -> tworzy stringa z wielką literą na początku
print( 'ala'.capitalize() ) # Ala

# count -> ilość wystąpienia danego łańcucha znaków w stringu
print( 'Ola ma kota. Ola ma psa'.count('Ola') ) # 2

# center -> centruje string, między podane elementy (default to spacja)
print( 'Hello'.center(15,'-') ) # -----Hello-----

# startswith -> sprawdzenie czy string zaczyna się jakimś wybranym string
print( welcome_text.startswith('Hello') ) # True

# endswith -> sprawdzenie czy string kończy się jakimś wybranym string
print( welcome_text.endswith('Hello') ) # False
print( welcome_text.endswith('ld!') ) # True

# find -> wyszukiwanie stringa w stringu od lewej strony, -1 nie występuje (nie ma szukanego stringa),
# zwraca wartość indeksu pod, którym jest szukany string
print( welcome_text.find('Patryk') ) # -1
print( welcome_text.find('Hello') ) # 0
print( welcome_text.find('World') ) # 6
print( welcome_text.find('!') ) # 11
print( 'Ola ma kota. Ola ma psa'.find('Ola') ) # 0 -> od lewej

# rfind -> wyszukiwane stringa w stringu od prawej strony (od końca)
print( 'Ola ma kota. Ola ma psa'.rfind('Ola') ) # 13

# isalnum -> czy dany string jest liczbą całkowitą
print( '23456'.isalnum() ) # True
print( '23456.656'.isalnum() ) # False
print( '23456 p'.isalnum() ) # False

# isalpha -> czy dany string to tylko znaki alfabetu
print( '234234'.isalpha() ) # False
print( 'piesek'.isalpha() ) # True
print( ' piesek'.isalpha() ) # False -> spacja nie jest znakiem alfabetu
print( 'piesek2'.isalpha() ) # False

# islower -> czy string składa się tylko z małych liter
print( 'test'.islower() ) # True
print( 'tesT'.islower() ) # False
print( 'TEST'.islower() ) # False

# isupper -> czy string składa się tylko z małych liter
print( 'TEST'.isupper() ) # True
print( 'tesT'.isupper() ) # False
print( 'test'.isupper() ) # False

# isspace -> czy string ma tylko białe znaki(spacje)
print( '   '.isspace() ) # True
print( '   \n\n\t'.isspace() ) # True
print( 'test'.isspace() ) # False
print( 'test   '.isspace() ) # False

# join -> połączenie stringa za pomocą innego stringa
print( '-|-'.join( ['Ala','Ola','Adam'] ) ) # Ala-|-Ola-|-Adam

# lower -> zmiana na wszystkie małe litery
print( 'Hello World!'.lower() ) # hello world!

# upper -> zmiana na wszystkie wielkie litery
print( 'Hello World!'.upper() ) # HELLO WORLD!

# swapcase -> zamiana wielkości liter
print( 'Hello World!'.swapcase() ) # hELLO wORLD!

# pozbycie się białych znaków w stringu od lewej strony
print( '   \n \t Hello free space world   .\n\n'.lstrip() )
# UWAGA! działa od białego znaku, gdy przed spacją jest znak, to już nie usunie białych znaków
print( '.   \n \t Hello free space world   .\n\n'.lstrip() ) # nie zmienia wgl stringa

print('---')
# pozbycie się białych znaków w stringu od prawej strony
print( '.   \n \t Hello free space world   \n\n'.rstrip() )

# pozbycie się białych znaków po obu stronach
print( '   \n \t Hello free space world   \n\n'.strip() )

# zamiana stringa na wybranego stringa
print( 'Ola ma kota. Ola ma psa.'.replace('Ola','Kaziu') ) # Kaziu ma kota. Kaziu ma psa.

# format -> formatowanie stringa
print( '''My name is {my_name}, I'am from {country}.'''.format(my_name = 'Patryk', country = 'Poland') )
print( '''My name is {my_name}, my favorite number is {number}.'''.format(my_name = 'Patryk', number = '8') )
print( '''My name is {0}, my favorite number is {1}.'''.format('Patryk', 8) )
print( '''My name is {}, my favorite number is {}.'''.format('Patryk', 8) )
# My name is Patryk, I'am from Poland.
# My name is Patryk, my favorite number is 8.





