# pomnożenie elementów listy z wykorzystaniem pętli for
from functools import reduce


list_data_1 = [1,2,3,4,5]
list_data_2 = []

for x in list_data_1:
    list_data_2.append(x * 2)
    print(list_data_2)

print(f'\nLista po zmianie FOR: {list_data_2}')
# lambda
sum = lambda a, b: a + b

print( sum(10,5) )
print( sum(20,30) )

#lambda w fukncji

def gen_func (n):
    return lambda a: a * n # zwrócona jest fukncja lambda, która zapamięta wartość n

doubler = gen_func(2)
print( f'Doubler z wartością 5: {doubler(5)}' )

tripler = gen_func(3)
print( f'Tripler z wartością 10: {tripler(10)}' )


# pomnożenie elementów listy z wykorzystaniem wyrażenia lambda
list_data_3 = [6,7,8,9,10]

print(f'\nLista nr.3: {list_data_3}')
# map -> stosuje funkcję na każdym elemencie listy*
result = map( lambda x: x * 2, list_data_3 ) # map zwraca iterator
list_data_4 = list(result) # iterator zmieniamy na listę

print(f'\nLista po zmianie map, LAMBDA: {list_data_4}\n')

# filter -> przyjmuje wyrażenie lambda, które zwróci true, sprawi, że dany element listy znajdzie się w wynikowej sekwencji

list_of_names = ['Patryk', 'Ola', 'Kuba', 'Bartłomiej']
print(list_of_names)

result_two = filter( lambda x: len(x) <=5, list_of_names )
list_of_names_2 = list(result_two)

print(f'Lista po zmianie filter, LAMBDA: {list_of_names_2}')

# reduce -> redukuje wszystkie elementy listy do pojedynczej wartości liczbowej

result_3 = reduce( lambda x,y: x + y,list_data_1 ) # y na początku 0
result_4 = reduce( lambda x,y: x + y,list_of_names )
print(type(result_3))
print(type(result_4))
print(f'Suma elementów pierwszej listy: {str(result_3)}')
print(f'Suma imion: {result_4}')





