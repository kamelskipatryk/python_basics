
def add_numbers(a,b,c):
    return a + b + c

def sum_list_elements(list_data):
    if len(list_data) == 0:
        print('Lista jest pusta.')
        return None
    result = 0
    for v in list_data:
        result += v
    return result

print( sum_list_elements([]) )
print( sum_list_elements([1,2,3]) )

# nie zwracamy żadnej wartości - bez return - nie wykonujemy żadnych obliczeń w funkcji
def print_list(list_data):
    if len(list_data) == 0:
        return
    for v in list_data:
        print(v)

print_list([])
print_list([1,2,3])

# return służy do wyjścia z funkcji lub do zwrócenia wartości

def print_list_above_3(list_data):
    if len(list_data) <= 3:
        return
    print(list_data)
    return

print_list_above_3(['a','b','c'])
print_list_above_3(['a','b','c','d','e','f'])













