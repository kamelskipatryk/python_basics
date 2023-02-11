
from time import sleep, time
from random import randint
from functools import wraps

def check_execution_time(function):
    @wraps(function)
    def wrapper(*args, **kwargs):
        before_function = time()
        result = function(*args, **kwargs)
        after_function = time()

        print(f'Execution time: {after_function - before_function}')
        return result

    return wrapper

@check_execution_time
def very_old_slow_function(text):
    sleep(randint(1, 3))
    return text

@check_execution_time
def very_old_slow_number(number):
    return number

#print(very_old_slow_function('Very old slow function'))

#print(check_execution_time(very_old_slow_function)('check_execution_time')) # = @check_execution_time before def
#print(check_execution_time(very_old_slow_number)(12))

print(very_old_slow_function('check_execution_time'))
print(very_old_slow_number(12))