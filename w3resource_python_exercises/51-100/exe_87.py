# get file size in python
import os

file_name = __file__

file_stats = os.stat(file_name)

print(file_stats)
print(f'File Size in Bytes is {file_stats.st_size}')
print(f'File Size in MegaBytes is {file_stats.st_size / (1024 * 1024)}')

file_size = os.path.getsize(__file__)
print("\nThe size of file is :",file_size,"Bytes")
print()


file = open(__file__)
file.seek(0, os.SEEK_END)
print("The size of main.py is :", file.tell(), "bytes")

#fff

