import json

input = '''
[
    {
        "id" : "001",
        "x" : "2",
        "name" : "Chuck"
    },
    {
        "id" : "009",
        "x" : "7",
        "name" : "Chuck"
    },
    {
        "id" : "007",
        "x" : "8",
        "name" : "James Bond"
    }
]
'''

info = json.loads(input)
print(info)
print('User count:', len(info), '\n')

for item in info:
    print('Name', item['name'])
    print('Id', item['id'])
    print('Attribute', item['x'], '\n')
    if item['name'] == 'James Bond':
        print('Wow! You found', item['name'] + '!')
