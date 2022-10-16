import os
import shutil

script_dir = os.path.dirname(__file__)

fh = open(script_dir + '/test.txt', 'w', encoding='utf-8')
fh.write('Dane źżćźćźćźć')
fh.close()

# zamiana nazwy pliku test na new_test
if not os.path.exists(script_dir + '/new_test.txt'):
    os.rename(script_dir + '/test.txt', script_dir + '/new_test.txt' )

print( os.path.getsize(script_dir + '/new_test.txt')) # rozmiar pliku w bajtach

print( os.path.isfile(script_dir + '/new_test.txt')) # True
print( os.path.isdir(script_dir + '/new_test.txt')) # False
print( os.path.isdir( './basics')) # True - > ścieżka relatywna

# kasowanie katalogu
if os.path.exists(script_dir + '/sub_dir'):
    os.rmdir(script_dir + '/sub_dir')

# tworzenie katalogu
if not os.path.exists(script_dir + '/sub_dir'):
    os.mkdir(script_dir + '/sub_dir')

# kasowanie pliku
if os.path.exists(script_dir + '/new_test.txt'):
    os.remove(script_dir + '/new_test.txt')

# zmiana cwd - aktualny katalog, gdzie skrypt wykonuje operacje
print('cwd:', os.getcwd())
os.chdir(script_dir)
print('cwd:', os.getcwd())

# kopiowanie pliku - działają relatywne ściezki, bo zostały wcześniej zmienione
if not os.path.exists('data_copy.dat'):
    shutil.copyfile('data.dat', 'data_copy.dat')




