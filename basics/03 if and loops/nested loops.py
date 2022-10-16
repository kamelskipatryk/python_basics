
lists_data = [
    [0,1,2,3,4],
    ['Ola', 'Ala', 'Patryk'],
    [10, 'Patryk', 20, 'Bożenka']
]

# iteracja po liście nadrzędnej (ukazanie innych list)
for l_data in lists_data:
    print(l_data)

print('')
# iteracja po wewnętrznych listach (ukazania wartości list)
for l_data in lists_data:
    for v in  l_data:
        print(v)







