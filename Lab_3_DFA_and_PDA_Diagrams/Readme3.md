# Lab 3: FSM and PDA Implementations

## Overview
This lab focuses on the design and implementation of a Finite State Machine (FSM) to recognize decimal strings divisible by 3 and a Pushdown Automaton (PDA) for the language \( L \), which recognizes strings in the form \( WCW^R \), where \( W \) is any binary string, \( C \) is a special symbol, and \( W^R \) is the reverse of \( W \).

## Task A: Finite State Machine (FSM) for Decimal Strings Divisible by 3

### 1. State Diagram
- Draw the state diagram of the FSM using the given state transitions.

### 2. Implementation
- A program is implemented in Python/C++/C/Java to simulate the FSM.

### 3. Test Cases
The FSM is validated on the following test cases:
- **"9"**: Accepted
- **"123"**: Accepted
- **"123456789"**: Accepted
- **"314159265358979"**: Accepted
- **"000000000"**: Accepted
- **""**: Rejected

## Task B: Pushdown Automaton (PDA) for Language \( L \)

### 1. State Diagram
- Draw the state diagram and state transition table of the PDA.

### 2. Implementation
- A program is implemented in Python/C++/C/Java to simulate the PDA.

### 3. Test Cases
The PDA is validated on the following test cases:
- **"10C01"**: Accepted
- **"110C011"**: Accepted
- **"101C11"**: Accepted
- **"101101"**: Rejected
- **""**: Rejected
- **"C"**: Rejected

## Implementation Details
- The state and top of the stack are printed during the execution of both the FSM and PDA to provide insight into the processing of the input strings.

## Files Included
- **fsm.py**: Implements the FSM for recognizing decimal strings divisible by 3.
- **pda.py**: Implements the PDA for recognizing strings in the form \( WCW^R \).

## How to Run
1. Ensure you have Python/C++/C/Java installed.
2. Run the scripts using:
   ```bash
   python fsm.py
   ```
   or
   ```bash
   python pda.py
   ```
3. Input the test strings when prompted to see if they are accepted by the respective automata.

## References
- "Introduction to Automata Theory, Languages, and Computation" by Hopcroft and Ullman.