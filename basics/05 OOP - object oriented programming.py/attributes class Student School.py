import random

class Student2:
    def __init__(self, name):
        self.name = name


class Student:
    def __init__(self, name, surname, age, city):
        self.name = name
        self.surname = surname
        self.age = age
        self.city = city
        self.school_name = None
        self.school_subjects = None

    def print_info(self):
        print(self.name, self.surname, self.age, self.city, self.school_name, self.school_subjects)

class School:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self.list_of_students = []
        self.school_subjects = ['IT', 'Math', 'Robotics']

    def add_student(self, student):
        if isinstance(student, Student): # czy przekazany obiekt jest instacją danej klasy
            self.list_of_students.append(student)
            student.school_name = self.name
            student.school_subjects = random.choice(self.school_subjects)
        else:
            print(student, "nie został dodany. Wybierz obiekt, który jest instancją klasy School.")

    def remove_student(self,student):
        if isinstance(student, Student):
            self.list_of_students.remove(student)
             
    def print_school_info(self):
        print('School name:', self.name, 'City:', self.city)
        print('Students:')
        for student in self.list_of_students:
            student.print_info()


student_1 = Student('Kasia', "Lis", 20, 'Kraków')
student_1.school_name = "Tech School"
student_1.country = "Poland" # dodanie dynamicznie kolejnego atrybutu
student_1.print_info()
print(student_1.country)

student_2 = Student('Adam', "Ajax", 23, 'Wrocław')

student_3 = Student2('Patryk')

print(' ')
school = School('Mechanic School', 'Inowrocław')
school.add_student(student_1)
school.add_student(student_2)
school.add_student(student_3)
school.print_school_info()
school.remove_student(student_1)
print(' ')
print('po usunięciu:')
school.print_school_info()
print('\nNie ma na liście, ale wciąż istnieje.')
student_1.print_info()






