
fh = open('test.txt', 'r') # otwiera handle do pliku i read
lines = fh.readlines()
fh.close()

for line in lines:
    print(line)
