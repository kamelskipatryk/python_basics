
class PartyAnimal:
    x = 0

    def __init__(self):
        print('I am constructed.')

    def party(self):
        self.x = self.x + 1
        print('So far', self.x)
    
    def __del__(self):
        print('I am destructed', self.x)

an1 = PartyAnimal()
an1.party()
an1.party()
an1.party()

print('')

an2 = PartyAnimal()
an2.party()
print(type(an2))
an2 = 55 # overwriting == destroying previous object and crate new obj
print(type(an2))
print('')
# print('dir:', dir(an1))

