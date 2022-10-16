
# Falsem jest:
# - False
# - 0, 0.0
# pusta lista []

my_list = [1]

if my_list:
    print('pełna')
else:
    print('pusta')

liczba = 10
liczba2 = 10
print(id(liczba))
print(id(liczba2))
print(id(10))

# wartości domyślne argumentów funkcji są ewaluowane tylko raz
# nigdy nie używaj czegoś co jest mutowalne jako parametr defaultowy
def foo(bar = []):
    bar.append('yolo')
    print(bar)

foo() # ['yolo']
foo(bar=[]) # ['yolo']
foo() # ['yolo', 'yolo']

def foo_2(bar = None):
    if bar is None:
        bar = []
    bar.append('yolo_2')
    print(bar)

foo_2() # ['yolo_2']
foo_2(bar=[]) # ['yolo_2']
foo_2() # ['yolo_2']

