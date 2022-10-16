# cwd - current working directory

import os

print('Absolute path to script file:', __file__) # g:\python testy\basics\06 files\path cwd script.py

script_dir = os.path.dirname(__file__)
print('Absolute path to script directory:', script_dir) # g:\python testy\basics\06 files

fh = open('new_file.txt', 'w')
fh.write('content!')
fh.close()

path_to_file = script_dir + '\\new_file_2.txt' 
print('Path to file:', path_to_file)

fh_2 = open( path_to_file, 'w' ) # podwójny \\ bo w stringu jest \
fh_2.write('content_2!')
fh_2.close()

