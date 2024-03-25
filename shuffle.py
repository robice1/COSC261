def shuffle(s, t):
    if not s:
        return {t}
    if not t:
        return {s}
    result = set()
    for shuffle_s in shuffle(s[1:], t):
        result.add(s[0] + shuffle_s)
    for shuffle_t in shuffle(s, t[1:]):
        result.add(t[0] + shuffle_t)
    return result

def shuffle_language(A, B):
    """
    Returns the shuffle A||B of languages A and B.
    Return the result as a set of strings, without duplicates.
    """
    result = set()
    for a in A:
        for b in B:
            result.update(shuffle(a, b))
    return result

