# Lab 8: Implementing a Predictive Parser (LL(1))

## Overview
This lab focuses on implementing a Predictive Parser using the LL(1) parsing technique. The parser will compute the FIRST and FOLLOW sets for a given context-free grammar (CFG), construct a parsing table, and parse input strings to determine if they are accepted by the grammar.

## Objectives
1. Understand the LL(1) Parsing technique.
2. Compute FIRST and FOLLOW sets for a given grammar.
3. Construct a Predictive Parsing Table.
4. Implement a Predictive Parser in Python.
5. Parse a given input string using the constructed table.

## Grammar
The following grammar will be used for the implementation:


## Implementation Steps
1. **Compute FIRST and FOLLOW Sets**: 
   - Implement functions to calculate the FIRST and FOLLOW sets for the non-terminals in the grammar.

2. **Construct the Parsing Table**: 
   - Based on the computed FIRST and FOLLOW sets, create a parsing table that maps non-terminals and input symbols to production rules.

3. **Implement the Predictive Parser**: 
   - Write a parser that uses the parsing table to analyze input strings and determine if they are valid according to the grammar.

4. **Test Cases**: 
   - Test the parser with the following input strings:
     - `id + id * id` (should be accepted)
     - `id + * id` (should be rejected)

## Output
- The program will display whether the input string is accepted or rejected by the grammar.
- It will also print the constructed parsing table and the steps taken during parsing.

## Usage
Run the `predictive_parser.py` script to execute the predictive parser. Follow the prompts to enter the input string for parsing.

### Example Input
```plaintext
id + id * id
```

### Example Output
```plaintext
Parsing successful: The input string is accepted by the grammar.
```

### Notes
- Ensure that the program correctly handles ε-productions and follows the LL(1) parsing rules.
- The implementation should be modular, with clear functions for computing FIRST and FOLLOW sets, constructing the parsing table, and parsing the input string.