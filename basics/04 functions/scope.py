
number = 12

def test_1():
    print(number) # 12, korzysta ze zmiennej globalnej

test_1()

def test_2():
    number = 100 # definiujemy zmienna lokalną
    print(number) # 100
    if 1 == 1:
        print(number) # 100
        if 2 == 2:
            number = 50 # modyfikujemy lokalną zmienną we fukncji
            print(number) # 50
    print(number) # 50, ostatni stan zmiennej lokalnej

test_2()
print(number) # 12, po za funkcjami korzysta ze zmiennej globalnej

print('\ntest_3')

def test_3():
    global number # odwołanie do globalnej zmiennej
    number = 5 # modyfikacja globalnej, NIE lokalnej
    print(number) # 5
    if 1 == 1:
        number = 6 # odwołujemy się również do zmiennej globalnej, mimo tego, że jesteśmy  w środku fukncji, poprzez wcześniejsze odwołanie globalne
        print(number) # 6

test_3()
print('global number:',number) # 6

# parametr
print('\ntest_4')

number = 10

def test_4(number):
    print('test_4 param:', number) # 66
    number = 20
    print('test_4 after change:', number) # 20

test_4(66)
print('global number after test_4():', number) # 10

# fukncja w funkcji
print('\ntest_5')

number = 10
def foo():
    print('foo() number:', number) # 10

def bar():
    number = 9 # zmienna przesłania globalną zmienną tylko w tej fukncji bar
    print('bar() number:' , number) # 9
    foo() # odwołujemy się tutaj nadal poprzez funkcję do zmiennej globalnej

bar()
print('global number after foo() and bar():', number) # 10

print('\ncheck_1 & check_2')

number = 10

def check_1():
    number = 12
    print('check_1() number:' , number) # 12
    def check_2(): # check_2 szuka wyżej definicji zmiennej number i znajduje number w check_1
        print('check_2() number:', number) # 12
    check_2()

check_1()
print('global number after check_1():', number) # 10

# if, while, try/except nie tworzy zmiennych lokalnych
print('\nif test')

if 1 == 1:
    data = 100 # zmienna globalna

print(data) # 100

if 2 == 1:
    next_data = 15

# print(next_data) # name 'next_data' is not defined, ponieważ if ma False







