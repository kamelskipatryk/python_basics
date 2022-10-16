
data = [0,1,2,3,4,5]

# przerwanie działania pętli
for i in data:
    if i == 3: break
    print(i*2)

print('')

# pomijanie/przerwanie jednej wybranej iteracji
for i in data:
    if i == 1 or i == 5: continue
    print(i)

if 10 > 2:
    pass



