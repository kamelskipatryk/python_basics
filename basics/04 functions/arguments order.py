# / - wszystko przed slash'em musi być przekazane jako parametr pozycyjny, nie może być nazwany
# * - wszystko po gwiazdce musi być przekazane jako parametr nazwany, nie może być pozycyjny



def print_car(brand, / ,name = 'concept', * ,year = 1960, color = 'black'):
    print(brand, name, year, color)

# name możemy przekazać dowolnie jak chcemy, albo pozycyjny albo nazwany
print_car('Toyota', 'Supra', year = 1987, color = 'yellow' )
print_car('Toyota', name = 'Supra', color = 'yellow', year = 1987 )
# print_car(brand = 'Toyota', name = 'Supra', color = 'yellow', year= 1987 ) # błąd brand, bo musi być pozycyjny
# print_car('Toyota', name = 'Supra', 1987, color = 'yellow' ) # błąd 1987, bo musi być nazwany


