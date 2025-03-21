# ALGORITHM_3_LFCO_2025_JJE.py
# This program builds a leftmost derivation tree for strings accepted by grammar G.
# Grammar G: S -> a S b | ε
# The tree is represented as a series of sentential forms in the leftmost derivation.

import ALGORITHM_2_LFCO_2025_JJE as AL2

def leftmost_derivation(string):
    """
    Constructs the leftmost derivation for the input string using grammar G.
    For a string in the language {a^n b^n}, the derivation is:
        S => a S b => a a S b b => ... => a^n S b^n => a^n ε b^n
    Returns a list of sentential forms representing the derivation.
    """
    if string == "":
        return ["S", "ε"]
    
    # Verify that the string is of the form a^n b^n
    n = len(string) // 2
    if string != "a" * n + "b" * n:
        return None  # The string is not generated by the grammar
    
    derivation = []
    current = "S"
    derivation.append(current)
    
    # For each 'a' (and corresponding 'b'), apply the rule S -> a S b
    for _ in range(n):
        current = current.replace("S", "a S b", 1)
        derivation.append(current)
    
    # Finally, replace the remaining S with ε
    current = current.replace("S", "ε", 1)
    derivation.append(current)
    
    return derivation

def print_derivation_tree(derivation):
    """
    Prints the derivation tree with increasing indentation for each derivation step.
    """
    if not derivation:
        print("The string is not in the language.")
        return
    indent = ""
    for step in derivation:
        print(indent + step)
        indent += "  "  # Increase indentation for each subsequent step
