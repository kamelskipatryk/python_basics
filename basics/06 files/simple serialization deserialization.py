import os
import pickle

script_dir = os.path.dirname(__file__)

number = 12342345457568567
list_data = ['cokolwiek', 5454]
str_data = 'Test żźłółół'

fh = open(script_dir + '/data.dat', 'wb')
# wrzucamy do pliku
pickle.dump(number, fh)
pickle.dump(list_data, fh)
pickle.dump(str_data, fh)
fh.close()

# ważna kolejność!
fh = open(script_dir + '/data.dat', 'rb')
# odczytujemy z pliku
number_info = pickle.load(fh)
list_info = pickle.load(fh)
str_info = pickle.load(fh)
fh.close()

print(number_info)
print(list_info)
print(str_info)

