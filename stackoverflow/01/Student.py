class Student:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname
        print('Constructor: ' + name + ' ' + surname)
    
    def __str__(self):
        return '__str__: ' + self.name + ' ' + self.surname
    
    def print_info_student(self):
        print('print_info_student: ' + self.name + ' ' + self.surname)