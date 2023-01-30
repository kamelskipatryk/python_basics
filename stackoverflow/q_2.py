# https://stackoverflow.com/questions/72899/how-do-i-sort-a-list-of-dictionaries-by-a-value-of-the-dictionary?rq=1
# How do I sort a list of dictionaries by a value of the dictionary?

list0 = [{'name': 'Homer', 'age': 39}, {'name': 'Bart', 'age': 10}]

newlist = sorted(list0, key=lambda d: d['name'])

print(newlist)