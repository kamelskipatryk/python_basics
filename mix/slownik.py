nasz_slownik = {32 : 'patryk', 'pawel' : 15, (1, 2) : 'wow'}

print(nasz_slownik[32])
print(nasz_slownik.get('pawel'))
print(nasz_slownik.get((1, 3), -60))