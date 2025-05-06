# Lab 5: Lexical Analyzer

## Overview
This lab focuses on the design and implementation of a lexical analyzer (lexer) for a custom programming language. The lexer identifies different types of tokens, handles errors, and generates a symbol table with additional metadata.

## Tasks
1. **Token Categories**: The lexer distinguishes the following token categories:
   - **Keywords**: e.g., `if`, `else`, `while`, `return`, `int`, `float`
   - **Identifiers**: Variable and function names following naming conventions.
   - **Operators**: e.g., `+`, `-`, `*`, `/`, `%`, `==`, `!=`, `<`, `>`, `<=`, `>=`, `&&`, `||`
   - **Delimiters**: e.g., `;`, `,`, `{`, `}`, `(`, `)`
   - **Literals**: Integer, floating point, string, and character constants.
   - **Comments**: Single-line (`// this is a comment`) and multi-line (`/* multi-line comment */`).

2. **Symbol Table**: Implement a symbol table to store:
   - Identifiers
   - Data types
   - Memory locations
   - Line numbers

3. **Error Handling**: The lexer handles various lexical errors:
   - **Invalid Identifiers**: Detect incorrect variable names (e.g., starting with a number).
   - **Unterminated Strings or Comments**: Handle cases where strings or comments are not properly closed.
   - **Illegal Characters**: Detect unexpected special symbols.

## Output Format
- The lexer prints a tokenized output with token types.
- Displays a symbol table.
- Logs lexical errors in a separate file.

## Files
- `q1.py`: Implementation of the lexical analyzer.
- `errorlog.log`: Log file for lexical errors (generated during execution).

## Usage
Run the `q1.py` script to analyze input code. The output will display the categorized tokens, the symbol table, and any lexical errors encountered.

### Example Input
```plaintext
int a = 5;
if (a > 3) {
    // Check condition
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
- Ensure that comments and spaces are ignored, and tokens are correctly categorized.
- The symbol table will include metadata for each identifier.