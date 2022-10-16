import user # przy imporcie wykonywany cały kod, dlatego -> User: Ola
from manager import Manager # można bezpośrednio odwoływać się do Manager

print('main:', user.user_1) # main: User: Ola

employee_1 = user.Employee('Patryk')
print('main:', employee_1)

manager_1 = Manager('Jola')
print('main:', manager_1)