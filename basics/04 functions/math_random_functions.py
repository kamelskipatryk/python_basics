import math
import random

print( str(12) )
print( str([12, 34]) )

number = int('123')
print(type(number))

float_num = float('45.15') # kropka! nie przecinek, bo nie może skonwertować
print( type(float_num) )
float_num *= 2
print(float_num)
#--------------------------------------------------------------------------------------
# wartość bezwględna
print( abs(9) ) # 9
print( abs(-9) ) # 9
print( abs(-9.1) ) # 9.1

# zaokrąglenie do góry/sufitu, liczby całkowite
print( math.ceil(20.50) ) # 21
print( math.ceil(10.000001) ) # 11
print( math.ceil(-1.000001) ) # -1
print( math.ceil(-1.999999) ) # -1

# zaokrąglenie do dołu/podłogi, liczby całkowite
print( math.floor(20.50) ) # 20
print( math.floor(20.51) ) # 20
print( math.floor(10.000001) ) # 10
print( math.floor(-1.000001) ) # -2
print( math.floor(-1.999999) ) # -2

# największa liczba z przekazanych wartości
print( max(1,3,556,-9,0,43) ) # 556
print( max([1,3,556,-9,0,43]) ) # 556, lista
print( max((1,3,556,-9,0,43)) ) # 556, krotka(tupla)

# najmniejsza liczba z przekazanych wartości
print( min(1,3,556,-9,0,43) ) # -9
print( min([1,3,556,-9,0,43]) ) # -9, lista
print( min((1,3,556,-9,0,43)) ) # -9, krotka(tupla)

# podnoszenie do potęgi
print( 2 ** 3) # 8
print( pow(2, 3)) # 8

# pierwiastek kwadratowy
print( math.sqrt(16) ) # 4.0

# zaokrąglenie liczy do podanej ilości miejsc po przecinku
print( round(20.52345345, 3) ) # 20.523
print( round(20.52345345, 2) ) # 20.52
print( round(20.52345345, 1) ) # 20.5
print( round(20.58345345, 1) ) # 20.6
print( round(20.495345345, 0) ) # 20.0

# liczba losowa float
print( random.random() ) # uzyskamy float od 0 do 1 np. 0.8795342754274849
print( random.random() * 100 ) # uzyskamy float od 0 do 99 np. 90.03265860001389
print( int(random.random() * 100) ) # uzyskamy int od 0 do 99 np. 8

# losowy element z listy
print( random.choice( [0,1,2,3,4,5] ) ) # np. 4
print( random.choice( ['0,1,2,3,4,5', 'Ola', 'Paweł', 'Zirka'] ) ) # np. Zirka

# losowa wartość z zakresu -> start, stop, step
print( random.randrange(-10, 30) ) # np. 3
print( random.randrange(-10, 30, 5) ) # np. 20

# losowe elementy w liście
list_data = [0,1,2,3,4,5,6,7,8,9]
random.shuffle(list_data)
print(list_data) # np. [5, 9, 6, 2, 0, 7, 3, 8, 1, 4]



