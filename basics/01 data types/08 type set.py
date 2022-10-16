
setData = {0, 1, 2, 3, 4, 5}

# dodawanie wartości do setData
setData.add(6)

print(setData)

setData.add(6) # wartość nie będzie dodana, bo już jest w zestawie

# kasowanie wartości w secie
setData.discard(0)

print(setData)

# iterowanie elementów w secie
for v in setData:
    print(v)

print(' ')
# frozenset - niemutowalny
frozen = frozenset(setData)

# frozen.add(4) # błąd

# iterowanie elementów w frozen secie
for v in frozen:
    print(v)
