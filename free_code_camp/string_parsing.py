
data = 'From stephen.marquard@uct.ac.za Sat jan 5 09:14:16 2008'

words = data.split()
email = words[1]
pieces = email.split('@')
print(pieces[1])




