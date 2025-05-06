# Lab 4: Lexical Analyzer

## Overview
This lab focuses on the design and implementation of a lexical analyzer (lexer) that processes input code, ignoring redundant spaces, tabs, newlines, and comments. The lexer classifies tokens into keywords, identifiers, numbers, operators, and delimiters.

## Tasks
1. **Basic Input and Output Functionality**: Set up the main function and implement a tokenizer to split input into raw tokens.
2. **Token Classification**: Implement functions to classify tokens as keywords, identifiers, numbers, operators, and delimiters.
3. **Ignore Whitespace and Comments**: Extend functionality to skip whitespace characters and comments.
4. **Identifier Length Restrictions**: Add logic to truncate identifiers exceeding a specified length and issue warnings.

## Files
- `q1.py`: Implementation of the lexical analyzer.
- `q2.py`: Additional functionalities or variations (if applicable).

## Usage
Run the `q1.py` script to analyze input code. The output will display the classified tokens, ignoring comments and unnecessary whitespace.

### Example Input
```plaintext
/* This is a test */
int a = 5;
if (a > 3) { // Check condition
    a++;
}
```

### Example Output
```plaintext
Keyword: int
Identifier: a
Operator: =
Number: 5
Keyword: if
Identifier: a
Operator: >
Number: 3
Delimiter: (
Delimiter: )
Delimiter: {
Identifier: a
Operator: ++
Delimiter: }
```

### Notes
- Identifiers are truncated to a maximum length of 31 characters, with a warning issued for truncation.
- The lexer handles both single-line (`//`) and multi-line (`/* ... */`) comments.