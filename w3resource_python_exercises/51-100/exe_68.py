def getSum(number):
    sum = 0
    for digit in str(number): 
      sum += int(digit)      
    return sum
   
number_1 = 12
print(getSum(number_1))
print(getSum(18))