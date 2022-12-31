
counts = {}
text = input('Enter the text: ')
words = text.split()
print(type(words[0]))

for word in words:
    counts[word] = counts.get(word, 0) + 1

print(counts)


