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
