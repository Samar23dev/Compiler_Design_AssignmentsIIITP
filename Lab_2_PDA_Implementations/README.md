# Lab 2: PDA for Equal Numbers of 0s and 1s

## Overview
This lab focuses on designing and implementing a Pushdown Automaton (PDA) that accepts all strings having an equal number of `0`s and `1`s over the input symbol {0, 1} for the language \(0^n 1^n\) where \(n \geq 1\).

## Task Description
1. **Transition Diagram**: Draw the transition diagram for the given PDA. Label all states and transitions clearly.
2. **Implementation**: Implement the PDA in Python and test it with the following inputs:
   - `0011`
   - `000111`
   - `01`
   - `001`
3. **Modification**: Modify the PDA to accept strings where the number of `0`s and `1`s are equal but can appear in any order (e.g., `0110`, `1010`).
4. **Edge Case Testing**: Using the modified PDA, implement a program that checks whether the number of `0`s and `1`s are equal for strings over the input alphabet {0, 1}. Test it with edge cases like:
   - Empty string \( \epsilon \)
   - Unequal strings like `00011`
   - Random strings like `010110`

## Files Included
- **q1.py**: Implements the PDA for the language \(0^n 1^n\).
- **q2.py**: Implements the modified PDA for equal numbers of `0`s and `1`s in any order.

## Concepts Covered
- Pushdown Automata (PDA)
- Transition diagrams
- Stack operations for counting

## How to Run
1. Ensure you have Python installed.
2. Run the scripts using:
   ```bash
   python q1.py
   ```
   or
   ```bash
   python q2.py
   ```
3. Input the test strings when prompted to see if they are accepted by the PDA.

## References
- "Introduction to Automata Theory, Languages, and Computation" by Hopcroft and Ullman.