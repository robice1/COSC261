def all_subsets(s):
    s = list(s)
    if len(s) == 0:
        return [set()]
    subsets = []
    first = s[0]
    remaining = s[1:]
    subsets_without_first = all_subsets(remaining)
    subsets.extend(subsets_without_first)
    for subset in subsets_without_first:
        subsets.append({first} | subset) 
    return subsets

print({1} in all_subsets({0, 1, 2}))
