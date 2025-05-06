# Lab 6: FIRST Set Computation

## Overview
This lab focuses on implementing a program that computes the FIRST set of a given Context-Free Grammar (CFG). The FIRST set is a fundamental concept in compiler design and parsing.

## Understanding FIRST Set
1. **What is the FIRST Set?**
   - The FIRST set of a non-terminal in a CFG is the set of terminals that begin the strings derivable from that non-terminal. If the non-terminal can derive the empty string (ε), then ε is also included in the FIRST set.

2. **Rules for Computing the FIRST Set:**
   - If \( X \) is a terminal, then \( FIRST(X) = \{ X \} \).
   - If \( X \) is a non-terminal and \( X \rightarrow Y_1 Y_2 \ldots Y_k \) is a production:
     - Add \( FIRST(Y_1) \) to \( FIRST(X) \) except for ε.
     - If \( Y_1 \) can derive ε, then add \( FIRST(Y_2) \), and so on.
     - If all \( Y_i \) can derive ε, then add ε to \( FIRST(X) \).

### Example
For the grammar: