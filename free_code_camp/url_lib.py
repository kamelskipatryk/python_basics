import urllib.request, urllib.parse, urllib.error

fhand = urllib.request.urlopen('http://data.pr4e.org/romeo.txt')
#print(type(fhand))
for line in fhand:
    print(line.decode().strip())

print('')

fhand_2 = urllib.request.urlopen('http://www.dr-chuck.com/page1.html')
#print(type(fhand))
for line in fhand_2:
    print(line.decode().strip())

print('')

fhand_3 = urllib.request.urlopen('http://www.dr-chuck.com/page1.html')
counts = {}
for line in fhand_3:
    words = line.decode().split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
print(counts)



