# Compiler Lab Project

## Overview
This project consists of a series of labs focused on various aspects of compiler design and implementation. Each lab covers different topics, including lexical analysis, parsing techniques, and grammar analysis. The goal is to provide a comprehensive understanding of compiler construction and the principles behind it.

## Labs Overview

### Lab 1: DFA Implementation
- **Objective**: Design and implement Deterministic Finite Automata (DFA) to recognize specific patterns in input strings.
- **Files**:
  - `q1DFA.py`: Implementation of the DFA for a specific pattern.
  - `q21.py`: Additional DFA implementations or variations.
  - `q2DFA.py`: Another DFA implementation for different patterns.

### Lab 2: Pushdown Automata (PDA)
- **Objective**: Design and implement Pushdown Automata (PDA) to accept specific languages.
- **Files**:
  - `q1.py`: Implementation of a PDA that accepts strings with a specific pattern.
  - `q2.py`: Another PDA implementation for different patterns.

### Lab 3: Finite State Machines (FSM) and PDA
- **Objective**: Design and implement FSM and PDA for recognizing specific languages.
- **Files**:
  - `q1.py`: Implementation of an FSM to recognize decimal strings divisible by 3.
  - `q2.py`: Implementation of a PDA for the language L, recognizing strings in the form WCW^R.
  - `q11.py`, `q22.py`: Additional implementations or variations.

### Lab 4: Lexical Analyzer
- **Objective**: Implement a lexical analyzer that processes input code, ignoring redundant spaces, comments, and classifying tokens.
- **Files**:
  - `q1.py`: Implementation of the lexical analyzer.
  - `q2.py`: Additional functionalities or variations.

### Lab 5: Compiler Design
- **Objective**: Implement a lexical analyzer that identifies different types of tokens, handles errors, and generates a symbol table.
- **Files**:
  - `q1.py`: Implementation of the lexical analyzer.
  - `qpilot.py`: Additional functionalities or variations.
  - `errorlog.log`: Log file for lexical errors.

### Lab 6: FIRST Set Computation
- **Objective**: Implement a program that computes the FIRST set of a given Context-Free Grammar (CFG).
- **Files**:
  - `first.py`: Implementation to compute the FIRST set.

### Lab 7: FOLLOW Set Computation
- **Objective**: Implement a program that computes the FOLLOW set of a given Context-Free Grammar (CFG).
- **Files**:
  - `follow.py`: Implementation to compute the FOLLOW set.

### Lab 8: Predictive Parser (LL(1))
- **Objective**: Implement a Predictive Parser using the LL(1) parsing technique.
- **Files**:
  - `predictive_parser.py`: Implementation of the predictive parser.

### Lab 9: LR Bottom-Up Parser
- **Objective**: Implement an LR Bottom-Up Parser for a given grammar.
- **Files**:
  - `lr_parser.py`: Implementation of the LR parser.

## Usage
To run any of the labs, navigate to the respective lab directory and execute the corresponding Python script. Ensure that you have Python installed on your system.

### Example
For Lab 1, you can run:
```bash
python q1DFA.py
```

## Author
Samar Mittal  
IIIT Pune, CSE

## Conclusion
This project serves as a comprehensive guide to understanding the principles of compiler design and implementation. Each lab builds upon the previous one, providing a solid foundation in the various components of a compiler.