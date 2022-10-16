
playing = input('Czy chcesz zagrać? tak/nie: ')
score = 0

if playing.lower() != 'tak':
    print('Wyszedłeś z programu.')
    quit()

print('Ok, zaczynamy!')

print('\nPytanie numer 1')
answer = input('Jak nazywa się stolica Polski?\nOdp.: ')
if answer.lower() == 'warszawa': # lower zmienia wszystkie wielkie litery w małe
    score += 1
    print(f'Poprawna odpowiedź!\nWynik: {str(score)}/3')
else:
    print("Zła odpowiedź!")

print('\nPytanie numer 2')
answer = input('Jak nazywa się stolica Wielkiej Brytani?\nOdp.: ').lower() # lower od razu przy inpucie
if answer == 'londyn':
    score += 1
    print(f'Poprawna odpowiedź!\nWynik: {str(score)}/3')
else:
    print("Zła odpowiedź!")

print('\nPytanie numer 3')
answer = input('Jak nazywa się stolica Ukrainy?\nOdp.: ')
if answer.lower() == 'kijów':
    score += 1
    print(f'Poprawna odpowiedź!\nWynik: {str(score)}/3')
else:
    print("Zła odpowiedź!")

print(f'\nOstateczny wynik: {str(score)}/3')
if score == 3:
    print('Gratulacje! Zdobyłeś maksymalną liczbę punktów!')



