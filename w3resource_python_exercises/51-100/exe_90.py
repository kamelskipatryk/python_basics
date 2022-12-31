# Write a Python program to create a copy of its own source code.

with open(__file__) as file:
    print(file.read())

# text