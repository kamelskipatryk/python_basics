
class Employee:
    'Employee class describing company employee' # doc string
    # static variables for all objects based on Employee
    num_Employees = 0
    Employees_list = []

    def __init__(self, name):
        'Constructor for Employee' # doc string
        self.name = name

        Employee.num_Employees += 1
        print(self.name, 'number:', Employee.num_Employees)

        Employee.Employees_list.append(self) # dodaje obiekt do list -> self wskazuję na utworzony obiekt
    
    def print_all_Employees(self):
        for emp in Employee.Employees_list:
            print(emp.name)

employee_1 = Employee('Adam')
employee_2 = Employee('Piotr')
employee_3 = Employee('Karol')
employee_4 = Employee('Kasia')

print('Employee.num:', Employee.num_Employees)
print(' ')
print(Employee.Employees_list)
print(' ')
employee_1.print_all_Employees()
print(' ')

# help(Employee) # -> informację o obiekcie
print(Employee.__doc__) # Employee class describing company employee
print(Employee.__name__) # Employee
print(Employee.__module__) # __main__

# sprawdzamy czy podany atrybut znajduje się w danym obiekcie
print('name attr in Employee:', hasattr(employee_1, 'name')) #-> name attr in Employee: True
print('city attr in Employee:', hasattr(employee_1, 'city')) #-> name attr in Employee: False
employee_1.city = 'Waw'
print('city attr in Employee:', hasattr(employee_1, 'city')) #-> name attr in Employee: True

# pobranie wartości atrybutu z danego obiektu
print('get city attr in Employee:', getattr(employee_1, 'city')) #-> get city attr in employee_1: Waw

# ustawienie nowej wartości attr w obiekcie
setattr(employee_1, 'city', 'Poz')
print('get city attr in Employee:', getattr(employee_1, 'city')) #-> get city attr in employee_1: Poz


