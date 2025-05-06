# Lab 1: DFA Implementations

## Overview
This lab focuses on constructing and implementing two Deterministic Finite Automata (DFAs) to process strings over the alphabet {0, 1}. The DFAs are designed to recognize specific patterns in input strings.

## Task Description
### Part 1: DFA for Strings with the Substring 000
- **Objective**: Design a DFA that accepts strings containing the substring `000`. The DFA should handle:
  - Strings that may contain additional `0`s or `1`s after or before `000`.
  - Verification if the string contains exactly `000`, at least `000`, or does not contain `000` at all.
  - Testing for strings with varying lengths, including empty strings.

### Part 2: DFA for Strings Without Consecutive 000's
- **Objective**: Design a DFA that accepts strings with no consecutive `000`s. The DFA should handle:
  - Any sequence of `1`s is valid.
  - Intermittent `0`s are valid, but two or more consecutive `000`s lead to rejection.
  - Strings of any length, including empty strings, should be handled.

## Files Included
- **q1DFA.py**: Implements the DFA for strings containing the substring `000`.
- **q2DFA.py**: Implements the DFA for strings without consecutive `000`s.

## Concepts Covered
- DFA construction
- State transitions
- Input string recognition

## How to Run
1. Ensure you have Python installed.
2. Run the scripts using:
   ```bash
   python q1DFA.py
   ```
   or
   ```bash
   python q2DFA.py
   ```
3. Input a string when prompted to see if it is accepted by the respective DFA.

## References
- "Introduction to Automata Theory, Languages, and Computation" by Hopcroft and Ullman.