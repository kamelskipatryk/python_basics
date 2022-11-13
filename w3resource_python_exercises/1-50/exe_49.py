import os

script_dir = os.path.dirname(__file__)
print('Absolute path to script directory:', script_dir)

print(script_dir)

files = os.listdir('./w3resource_python_exercises')
print(files)

print('')

for file in files:
    print(file)





