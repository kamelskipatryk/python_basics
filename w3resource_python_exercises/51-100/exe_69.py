int_1 = int(input("Input first number: "))
int_2 = int(input("Input second number: "))
int_3 = int(input("Input third number: "))

list = [int_1,int_2,int_3]

list.sort()

print(list)

x = int(input("Input first number: "))
y = int(input("Input second number: "))
z = int(input("Input third number: "))

a1 = min(x, y, z)
a3 = max(x, y, z)
a2 = (x + y + z) - a1 - a3
print("Numbers in sorted order:", a1, a2, a3)




