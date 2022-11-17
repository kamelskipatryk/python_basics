import time

# get the start time
st = time.time()

# main program
# find sum to first 1 million numbers
sum_x = 0
for i in range(1000000):
    sum_x += i

# wait for 3 seconds
#time.sleep(3)
print('Sum of first 1 million numbers is:', sum_x)

# get the end time
et = time.time()

# get the execution time
elapsed_time = et - st
final_elapsed_time_minutes = elapsed_time/60
print('Execution time:', elapsed_time, 'seconds')
print('Execution time:', final_elapsed_time_minutes, 'minutes')

st = time.time()
# your code
sum_x = 0
for i in range(1000000):
    sum_x += i
#time.sleep(3)
print('Sum:', sum_x)

elapsed_time = time.time() - st
print('Execution time:', time.strftime("%H:%M:%S", time.gmtime(elapsed_time)))

import time
def sum_of_n_numbers(n):
    start_time = time.time()
    s = 0
    for i in range(1,n+1):
        s = s + i
    end_time = time.time()
    return s,end_time-start_time

n = 500
print("\nTime to sum of 1 to", n ,"and required time to calculate is:",sum_of_n_numbers(n))



