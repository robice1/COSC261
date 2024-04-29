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

def generating_nts(cfg_str):
    """returns a set containing all the generating non-terminals in the given CFG, where
    cfg_str is a multi-line string representing a CFG"""
    cfg_dict = cfg_str_to_dict(cfg_str)
    generating = set()
    while True:
        new_generating = generating.copy()
        for nt, rhs_list in cfg_dict.items():
            for rhs in rhs_list:
                if all(symbol.islower() or symbol.isdigit() or symbol == '_' or symbol in generating for symbol in rhs):
                    new_generating.add(nt)
                    break
        if new_generating == generating:
            break
        generating = new_generating
    return generating

cfg = """S=X|Y
W=_
X=Z1|0Z|1Y|Y0
Y=1|0|X
Z=_"""
print(sorted(generating_nts(cfg)))