import os

script_dir = os.path.dirname(__file__)

f_name = input('Enter file: ')
if len(f_name) < 1: f_name = 'text.txt'
f_hand = open(script_dir + '//' + f_name)

# make a counter for words
counts_dict = {}
for line in f_hand:
    line = line.rstrip()
    words = line.split()
    for word in words:
        counts_dict[word] = counts_dict.get(word, 0) + 1

# find most common word
largest = -1
most_common_word = None
for k, v in counts_dict.items():
    if v > largest:
        largest = v
        most_common_word = k

print(most_common_word, largest)


