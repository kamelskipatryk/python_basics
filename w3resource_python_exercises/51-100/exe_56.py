import os

info = os.get_terminal_size()

print(info)
print('Colums:', info.columns)
print('Lines:', info.lines)
print(type(info))