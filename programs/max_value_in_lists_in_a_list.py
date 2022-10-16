# mój pierwszy samodzielny, wymyślony program
# program sprawdzający największą wartość w listach w liście

lists_of_numbers = [[0,1,2,3,4,5,777.9,7,8,9],[10,111,12,13,14,15,16,17,18,19,30,31],[20,21,22,23,24,25,26,27,28,29],[-999]]
list_of_max_values = []

for list_of_number in lists_of_numbers:
    print(list_of_number)
    max_number = max(list_of_number)
    list_of_max_values.append(max_number)

print(max(list_of_max_values))