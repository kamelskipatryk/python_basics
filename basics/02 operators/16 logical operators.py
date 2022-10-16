
# operator and - zwraca wartość True jeśli obie strony wyrażenia mają wartość True
print('AND\n')
print( True and True ) # True
print( True and False ) # False
print( False and True ) # False
print( False and False ) # False

print ( 8 > 3 and 3 == 3 ) # True
print ( 4 >= 4 and 1 >= 10 ) # False
print ( 10 == 5 and 3 > 1 ) # False

if 5 == 5 and 10 > 4:
    print('True, bo oba warunki spełnione.')

task_today_1 = True
lines_of_code_written = 100
hours_of_day = 15

if task_today_1 == True and lines_of_code_written >= 50 and hours_of_day >= 15:
    print('Go home man!')

# operator or - zwraca True jeśli przynajmniej jedna strona ma True
print('\nOR\n')
print( True or True ) # True
print( True or False ) # True
print( False or True ) # True
print( False or False ) # False

print ( 8 > 3 or 3 == 3 ) # True
print ( 4 >= 4 or 1 >= 10 ) # True
print ( 10 == 5 or 3 > 1 ) # True
print ( 10 == 5 or 3 > 4 ) # False

if 'Ania' == 'Ania' or 10 == 1:
    print('True, bo pierwszy warunek spełniony.')

# operator not - odwraca wartość logiczną
print('\nNOT\n')

print( not True ) # False
print( not False ) # True

print ( not ( 10 == 10 ) ) # False
print ( not ( 4 < 1 ) ) # True
print ( not ( 5 == 5 and 3 > 1 ) ) # False

task_completed = False # zadanie nie było skończone

if not task_completed:
    print('Zadanie nie zostało wykonane')

