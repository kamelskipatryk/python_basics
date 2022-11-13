import profile

def sum():
    i_sum = 0
    for i in range(0,100):
        i_sum += i
        print(i_sum)

sum()
profile.run('sum()')