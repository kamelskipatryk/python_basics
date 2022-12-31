
raw_str = input('Enter a number: ')
try:
    ival = int(raw_str)
except:
    ival = -1

if ival > 0:
    print('Nice work, you put number correctly!')
else:
    print('Not a number!')