
text = 'Hello World'
print(text)
print( len(text) )
print( type(text) )

# pobranie wartości indeksu o numerze 6
print(text[6])

# pobranie wartości ostatniego elementu stringa
print( text[len(text) -1] )

#pobranie wartości indeksów od 0 do 4 -> Hello
print( text[0:5])

#mnożenie stringa razy 5
print( text * 5)

# łączenie stringów
text_2 = text + ' and Hello again'
print(text_2)

# wycinek stringa od wybranego id do końca
print( text_2[6:] )

# wycinek stringa od początku do 5 id
print( text_2[:6] )

# wyprintowanie co któryś element - UWAGA - pierwszy element zawsze się wyświetla
print(text_2[::2])

# wieloliniowy tekst w zmiennej
multi_line_text = """Pierwsza linia
Druga linia
Trzecia linia
"""

print(multi_line_text)

# wieloliniowy tekst - inna metoda + tabulacja, cudzysłow w stringu i backslash
multi_line_text_2 = 'Pierwsza linia_2\nDruga linia_2\nTrzecia \t linia \'\" \\'

print(multi_line_text_2)

# używanie f strings zamiast znaku +
text_3 = 'tekst!'
print('To jest mój ' + text_3)
print(f'To jest mój {text_3}')