import sys

tab = [1,3,5778,8,3,552]

print(sys.getsizeof(4))
print(sys.getsizeof(tab))
print('')
a = sys.getsizeof(12)
print(a)
 
b = sys.getsizeof('geeks')
print(b)
 
c = sys.getsizeof(('g', 'e', 'e', 'k', 's'))
print(c)
 
d = sys.getsizeof(['g', 'e', 'e', 'k', 's'])
print(d)
 
e = sys.getsizeof({1, 2, 3, 4})
print('{1, 2, 3, 4}: '+ str(e) + ' bytes')
 
f = sys.getsizeof({1: 'a', 2: 'b', 3: 'c', 4: 'd'})
print(f)