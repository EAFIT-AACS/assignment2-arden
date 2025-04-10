def generate_accepted_strings():
    """
    Generates a list of strings that are accepted by grammar G (i.e., strings of the form a^n b^n).
    """
    accepted = []
    # For example, generate strings for n = 0, 1, 2, 3
    for n in range(7):
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
    
    output_file = "generated_strings.txt"
    
    with open(output_file, "w") as file:
        file.write("Accepted Strings:\n")
        accepted = generate_accepted_strings()
        for s in accepted:
            file.write(f"'{s}'\n")
            print(f"'{s}'")

        file.write("\nRejected Strings:\n")
        rejected = generate_rejected_strings()
        for s in rejected:
            file.write(f"'{s}'\n")
            print(f"'{s}'")

    print(f"Output saved in '{output_file}'.")
        
    return None

if _name_ == "_main_":
    main()
