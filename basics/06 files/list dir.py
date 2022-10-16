import os

print("Current working directory:", os.getcwd())
print('')

# lista folderów i plików znajdująca się w pracującym folderze
files = os.listdir('.')
# print(files) # current working dir

files = os.listdir('./programs')
# print(files)

files = os.listdir('./basics/01 data types')
# print(files)

# co jest wyżej od tego katalogu pracującego, ścieżki relatywnej
files = os.listdir('..')
# print(files)

files = os.listdir('../obs nagrywanie')
print(files)




