
def sum_numbers(*args):
    sum = 0
    for arg in args:
        sum += arg
    return sum


print('sum:', sum_numbers(2,3,4,5,8,88,3))

# *args -> return/spread tuple of arguments
# **kwargs -> return/spread dictionary of arguments


