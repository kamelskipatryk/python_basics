import math

print(math.gcd(10,20))
print(math.gcd(18,20))
print(math.gcd(183,209))
print(math.gcd(45,15))

print('...')

def gcd(x, y):
   gcd = 1   
   if x % y == 0:
       return y   
   for k in range(int(y / 2), 0, -1):
       if x % k == 0 and y % k == 0:
           gcd = k
           break 
   return gcd
print("GCD of 10 & 20 =",gcd(10, 20))
print("GCD of 4 & 6 =",gcd(4, 6))
print("GCD of 336 & 360 =",gcd(336, 360))


