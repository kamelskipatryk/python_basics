import os
import pickle

script_dir = os.path.dirname(__file__)

class Person:
    def __init__(self, name, surname, city):
        self.name = name
        self.surname = surname
        self.city = city
    
    def __str__(self):
        return str(self.name) + ' ' + str(self.surname) + ' ' + str(self.city)
    
person_1 = Person('Ania', 'Kowalska', 'Waw')
person_2 = Person('Elżbieta', 'Michałkowska', 'Poz')

people = [person_1, person_2]

fh = open(script_dir + '/people.dat', 'wb')
pickle.dump(people, fh)
fh.close()


fh = open(script_dir + '/people.dat', 'rb')
list_from_file = pickle.load(fh)
fh.close()

print(list_from_file)

for person in list_from_file:
    print(person)