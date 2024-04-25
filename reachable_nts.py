def cfg_str_to_dict(cfg_str):
    """Converts a multiline CFG string representation 
       of the form used in COSC261 quiz questions 
       into a dictionary represention, e.g.
       "S=ab|bA|BB|_" becomes {"S": ["ab", "bA", "BB", ""]}
    """
    nonterminals = {char for char in cfg_str if char.isupper()}.union({'S'})
    result = {nt: [] for nt in nonterminals}
    productions = cfg_str.splitlines()
    for production in productions:
        nt, rhs = production.split("=")
        rhs = rhs.replace("_", "") # Use "" for epsilon
        rhs_list = rhs.split("|")
        result[nt] = result[nt] + rhs_list
    return result


def reachable_nts(cfg_str):
    """returns a sorted list containing all the reachable non-terminals in the given CFG, 
    where cfg_str is a multi-line string representing a CFG in the format described
    in the info panel before Question 6."""
    cfg_dict = cfg_str_to_dict(cfg_str)
    reachable = set()
    reachable.add('S')
    changed = True
    while changed:
        changed = False
        
        for nt in list(reachable):
            for production in cfg_dict[nt]:
                for char in production:
                    if char.isupper() and char not in reachable:
                        reachable.add(char)
                        changed = True
    return reachable

cfg = "A=0A1"
print(sorted(reachable_nts(cfg)))