import os.path
print(os.path.isfile('new_file.txt'))
print(os.path.isfile('main.py'))

my_file = open('test.txt')
try:
   my_file.close()
   print("File found!")
except FileNotFoundError:
   print("File not found!")