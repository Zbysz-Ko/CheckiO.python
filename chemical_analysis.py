#!/usr/bin/env python3

""" Learning Python
    Task from Checkio.org - Unix Match part 2
"""
from re import findall, sub

def atoms(formula, limit):
    """ Create a list of chemical elements 
        which are in the amount of >= limit in the formula
        """
    result, formula = [], formula.translate(str.maketrans('[]', '()'))
    elements = sorted(set(findall(r'[A-Z][a-z]?', formula)))
    resub = [(r'(\w)(?=[A-Z(])', r'\1+'), (r'(\d)', r'*\1')]

    for p, r in resub:
        formula = sub(p, r, formula)

    for i in elements:
        for j in elements:
            locals()[j] = int(i==j)
        if eval(formula) >= limit:
            result.append(i)

    return result

print("Example:")
print(atoms("C2H5OH", 2))

# These "asserts" are used for self-checking
assert atoms("C2H5OH", 2) == ["C", "H"]
assert atoms("H2O", 2) == ["H"]
assert atoms("Mg(OH)2", 1) == ["H", "Mg", "O"]
assert atoms("K4[ON(SO3)2]2", 4) == ["K", "O", "S"]

print("The mission is done! Click 'Check Solution' to earn rewards!")
