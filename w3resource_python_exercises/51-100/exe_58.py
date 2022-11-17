
def sum_positive_ints(*numbers):
    sum = 0
    for number in numbers:
        if number > 0:
            sum += number
    return sum

print(sum_positive_ints(1,-1,1,-55,28))

n = int(input("Input a number: "))
sum_num = (n * (n + 1)) / 2
print("Sum of the first", n ,"positive integers:", sum_num)






