def n_copies(str, n):
    if len(str) < 2:
        return str*n
    string_2 = str[:2]
    n_string = string_2*n
    return n_string


print(n_copies('.', 3))


