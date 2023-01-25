import re

data = 'From stephen.marquard@uct.ac.za Sat jan 5 09:14:16 2008'

words = data.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])


data2 = r'C:\Users\W00lfie\Desktop\zdj\tkanina1.jpg'
my_list = re.split(r'[^a-zA-Z0-9\s]', data2)
file_name = my_list[-2] + r'.' + my_list[-1]
print(file_name)
#words2 = data2.split("\")
#print(words2)




