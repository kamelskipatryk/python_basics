
class User:
    def __init__(self, name):
        self.name = name
    
    def __str__(self):
        return 'User: ' + self.name

user_1 = User('Ola')
print(user_1) # od razu korzysta z metody __str__

class Employee(User):
    def __init__(self, name):
        User.__init__(self, name)
    
    def __str__(self):
        return 'Employee: ' + self.name



