
def get_names(array):
    names = []
    for dict in array:
        for key, value in dict.items():
            if key == 'name':
                names.append(value)
    return names


print(
    'get_names:',
    get_names([
        {'a': 1},
        {'name': 'Jane'},
        {},
        {'name':'Mark'},
        {'name':'Sophia'},
        {'b': 2}
    ])
)

def get_names_2(array):
    names = []
    for dict in array:
        if 'name' in dict:
            names.append(dict['name'])
        
    return names


print(
    'get_names_2:',
    get_names_2([
        {'a': 1},
        {'name': 'Jane'},
        {},
        {'name':'Mark'},
        {'name':'Sophia'},
        {'b': 2}
    ])
)



# if dict['name']










