# PDA Simulation Assignment

## Group Members
- Jerónimo Restrepo Ángel
- Juan Esteban Restrepo Orozco

## Environment and Tools
- **Operating System:** Ubuntu 20.04 (or later)  
- **Programming Language:** Python 3.8 (or higher)  
- **Development Tools:** Git, Visual Studio Code, Terminal

## Assignment Overview
This repository contains our submission for Assignment 2 of Formal Languages. The assignment is based on the context-free grammar:

S -> aSb | ε


We have implemented three distinct algorithms with a web interface to interact with them. Each algorithm addresses a different part of the formal language processing:

### Algorithms:

1. **Algorithm 1: String Generation**  
   - **Purpose:** Generate strings that belong to the language (accepted) and strings that do not belong (rejected) using the alphabet {a, b}.
   - **Details:**  
     - Accepted strings follow the pattern **aⁿbⁿ** (e.g., "", "ab", "aabb", "aaabbb").
     - Rejected strings are examples that do not meet this pattern.
   - **File:** `ALGORITHM_1_LFCO_2025_JJE.py`

2. **Algorithm 2: PDA Simulation**  
   - **Purpose:** Simulate a Pushdown Automaton (PDA) that recognizes strings generated by grammar G.
   - **Details:**  
     - The PDA processes the input string symbol by symbol, pushing a marker for every 'a' and popping for every 'b'.
     - The algorithm logs a detailed history of configurations (position, current symbol, and stack contents), which helps with debugging and understanding the PDA operation.
   - **File:** `ALGORITHM_2_LFCO_2025_JJE.py`

3. **Algorithm 3: Leftmost Derivation Tree**  
   - **Purpose:** Build a leftmost derivation tree (or list of sentential forms) for accepted strings by the grammar G.
   - **Details:**  
     - For any accepted string of the form **aⁿbⁿ**, the derivation is constructed starting from the start symbol S and repeatedly applying the production rule `S -> aSb` until S is replaced by ε.
     - The derivation tree is printed with increasing indentation to clearly display each step of the derivation.
   - **File:** `ALGORITHM_3_LFCO_2025_JJE.py`

## Web Server Overview

In addition to the command-line interface, we have implemented a Flask web server that allows you to interact with the algorithms through a simple front-end. The server provides three buttons that correspond to each of the algorithms. Upon clicking a button, the server makes a request to the appropriate algorithm and displays the results in a new page.

- **Algorithm 1**: Generates a list of accepted and rejected strings.
- **Algorithm 2**: Simulates a PDA and displays whether each string is accepted or rejected, along with the PDA's configuration history.
- **Algorithm 3**: Displays the leftmost derivation tree for accepted strings.

### Flask Web Interface:
- **URL:** `http://localhost:5000/`
- **Buttons:**
  - `Algoritmo 1`: View generated strings (accepted and rejected).
  - `Algoritmo 2`: Simulate the PDA and view configuration history.
  - `Algoritmo 3`: View the leftmost derivation tree for accepted strings.

## Detailed Implementation Overview

### Algorithm 1: String Generation
- **Functions:**
  - `generate_accepted_strings()`: Generates strings of the form **aⁿbⁿ** for several values of n.
  - `generate_rejected_strings()`: Provides sample strings that do not conform to the pattern **aⁿbⁿ**.
- **Main Function:**  
  Displays both the accepted and rejected strings and saves them in a file called `generated_strings.txt`.

### Algorithm 2: PDA Simulation
- **Functions:**
  - `run_pda(input_string)`: Simulates the PDA for the language **aⁿbⁿ**. It processes each symbol, updates the stack, and logs every configuration.
- **Main Function:**  
  Tests the PDA with the `generated_strings.txt` file created in Algorithm 1, prints whether each string is accepted or rejected, displays the configuration history, and saves the accepted strings in a file called `accepted_strings.txt` for use in the next algorithm.

### Algorithm 3: Leftmost Derivation Tree
- **Functions:**
  - `leftmost_derivation(string)`: Constructs the leftmost derivation for an input string using the grammar \(G\).
  - `print_derivation_tree(derivation)`: Prints the derivation steps with increasing indentation for clarity.
- **Main Function:**  
  Processes the accepted strings from Algorithm 2, printing their derivation trees.

## Prerequisites
1. **Create a virtual environment:**
```bash
python -m env env
```
2. **Install flask:**
```bash
pip install flask
```
3. **Create a requirements.txt file to define the flask version:**
```bash
Flask==2.1.2
```


## Running the Implementation

1. **Clone the Repository:**
```bash
git clone <repository_url>
cd <repository_directory>
```
2. **Run the Desired Algorithm:**
  (Run ALGORITHM_1)
   ```bash
   python3 ALGORITHM_1_LFCO_2025_JJE.py
   ```
   (Run ALGORITHM_2)
   ```bash
   python3 ALGORITHM_2_LFCO_2025_JJE.py
   ```
   (Run ALGORITHM_3)
   ```bash
   python3 ALGORITHM_3_LFCO_2025_JJE.py
   ```
   To run the Flask web interface, use the following command:
   ```bash
   python3 server.py
   ```

## Access the Web Interface
Once the Flask server is running, open a browser and navigate to http://localhost:5000/ to interact with the algorithms via the web interface.

## Expected Output Examples

1. *Algorithm 1: String Generation*
   bash
      'ab'
      'aabb'
      'aaabbb'
      'aaaabbbb'
      'aaaaabbbbb'
      'aaaaaabbbbbb'
      'a'
      'b'
      'abbb'
      'aaabb'
      'aba'
      'ba'
      'aab'
      'bba'
   
2. *Algorithm 2: PDA Simulation*

For each test string, the output displays:

- Whether the string is accepted or rejected.
- A history of configurations (position, current symbol, and the current state of the stack).

3. *Algorithm 3: Leftmost Derivation Tree*

For a string like "aabb", the output will display:
    bash
    Leftmost derivation for string: 'aabb'
    S
      a S b
        a S b b
          a ε b b
    ----------------------------------------
    

## References

- Kozen, D. C. (1997). Automata and Computability. Springer-Verlag. ISBN: 0387949070. DOI: 10.1007/978-1-4612-1844-9.
