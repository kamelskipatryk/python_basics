
class Student:
    def __init__(self, name:str) -> None:
        self.name = name
        self.grades = []
    
    def calculate_the_average(self):
        return sum(self.grades) / len(self.grades)
    
    def append_grade(self, grade):
        self.grades.append(grade)

bartek = Student('Kuba')
print(bartek.name)
print(bartek.grades)

bartek.append_grade(5)
print(bartek.grades)


