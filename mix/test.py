runda = 0
wynik1 = 0
wynik2 = 0
poprawne_odpowiedzi = ['kamien','papier','nozyczki']

def pobierz_wybor(gracz):
    while True:
        wybor_gracza = input(f'{gracz} podaj swoj wybor: ')
        if wybor_gracza in poprawne_odpowiedzi:
            return wybor_gracza
        else:
            print('podaj poprawna wartosc')

def sprawdz_wynik(wybor_gracza1, wybor_gracza2):
    if wybor_gracza1 == wybor_gracza2:
        print('remis')
        return 0
    
    wynik = {
        ('papier', 'kamien'): 1,
        ('kamien', 'nozyczki'): 1,
        ('nozyczki', 'papier'): 1,
    }

    return wynik.get((wybor_gracza1, wybor_gracza2), 2)
        
while runda < 3:

    wybor_gracza1 = pobierz_wybor('Gracz1')
    wybor_gracza2 = pobierz_wybor('Gracz2')
    wynik = sprawdz_wynik(wybor_gracza1, wybor_gracza2)

    if wynik == 1:
        print('Gracz_1 wygral')
        wynik1 += 1
    elif wynik == 2:
        print('Gracz_2 wygral')
        wynik2 += 1

    runda += 1
    

print('Gracz_1:', wynik1, 'vs Gracz_2:', wynik2)
