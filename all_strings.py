import itertools

def all_strings(alpha, length):
    if length == 0:
        return ['']
    strings = []
    for tuple in itertools.product(map(str, alpha), repeat=length):
        strings.append(''.join(tuple))
    return strings


print(len(all_strings({1, 2, 3, 4, 5, 6, 7, 8}, 1)))
