
counts = {}
names = ['marta', 'kuba', 'róża', 'kuba', 'marta']

for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1
print(counts)
print('-------------------------')
#---------------------------------
counts_2 = {'marta' : 1}
names_2 = ['marta', 'kuba', 'róża', 'kuba', 'marta']

for name_2 in names_2:
    counts_2[name_2] = counts_2.get(name_2, 0) + 1
print(counts_2)


