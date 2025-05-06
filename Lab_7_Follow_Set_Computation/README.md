# Lab 7: FOLLOW Set Computation

## Overview
This lab focuses on implementing a program that computes the FOLLOW set of a given Context-Free Grammar (CFG). The FOLLOW set is essential for parsing and syntax analysis in compiler design.

## Understanding FOLLOW Set
1. **What is the FOLLOW Set?**
   - The FOLLOW set of a non-terminal in a CFG is the set of terminals that can appear immediately to the right of that non-terminal in some sentential form. If the non-terminal can be the last symbol in a production, then the end-of-input marker (usually represented as $) is also included in the FOLLOW set.

2. **Rules for Computing the FOLLOW Set:**
   - If \( A \rightarrow \alpha B \beta \), then everything in \( FIRST(\beta) \) (except ε) is in \( FOLLOW(B) \).
   - If \( A \rightarrow \alpha B \) or \( A \rightarrow \alpha B \beta \) where \( FIRST(\beta) \) contains ε, then everything in \( FOLLOW(A) \) is in \( FOLLOW(B) \).
   - If \( B \) is the start symbol, then $ is in \( FOLLOW(B) \).

### Example
For the grammar: