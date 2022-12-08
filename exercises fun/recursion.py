def suma_for(liczba):
    suma = 0
    for i in range(liczba + 1):
        suma += i

    return suma

print(suma_for(3))

def suma_rekurencja(liczba):
    if liczba == 0: return 0
    return liczba + suma_rekurencja(liczba - 1)

print(suma_rekurencja(3))