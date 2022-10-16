
class Person:
    def __init__(self, name, surname, city):
        self.name = name
        self.surname = surname
        self.city = city
        print('Person constructor!')
    
    def print_person_data(self):
        print('Person.print_person_data:', self.name, self.surname, self.city)
    
person_1 = Person('Ola', 'Kowalska', "Krk")
person_1.print_person_data()

class Employee(Person):
    def __init__(self, name, surname, city, company_name, salary):
        Person.__init__(self, name, surname, city) # self - przekazujemy obiekt do konstruktora Person oraz atrybuty name,surname,city
        self.company_name = company_name
        self.salary = salary
        print('Employee constructor!')
    
    def print_employee_data(self):
        print('Employee.print_employee_data:', self.name, self.surname, self.company_name, self.salary)

print()
employee_1 = Employee('Kasia','Kot','Waw','Tech Ltd', 10000)
employee_1.print_person_data()
employee_1.print_employee_data()

print()
class Manager(Employee):
    def __init__(self, name, surname, city, company_name, salary, department):
        Employee.__init__(self, name, surname, city, company_name, salary)
        self.department = department
        print('Manager constructor!')

    def print_manager_data(self):
        print('Manager.print_manager_data:', self.name, self.surname, self.department)

manager_1 = Manager('Ania','X','Waw','Tech_2 Ltd', 15000, 'IT')
manager_1.print_manager_data()

