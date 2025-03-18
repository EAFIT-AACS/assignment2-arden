def generate_accepted_strings():
    """
    Generates a list of strings that are accepted by grammar G (i.e., strings of the form a^n b^n).
    """
    accepted = []
    # For example, generate strings for n = 0, 1, 2, 3
    for n in range(4):
        string = "a" * n + "b" * n
        accepted.append(string)
    return accepted

def generate_rejected_strings():
    """
    Generates a list of strings that do not belong to the language of grammar G but use the same alphabet {a, b}.
    """
    # Some examples of rejected strings (not of the form a^n b^n)
    rejected = ["a", "b", "abbb", "aaabb", "aba", "ba", "aab", "bba"]
    return rejected

def main():
    strings_generated = []

    accepted = generate_accepted_strings()
    for s in accepted:
        print(f"'{s}'")
        strings_generated.append(s)
        
    rejected = generate_rejected_strings()
    for s in rejected:
        print(f"'{s}'")
        strings_generated.append(s)
        
    return strings_generated

if _name_ == "_main_":
    main()
