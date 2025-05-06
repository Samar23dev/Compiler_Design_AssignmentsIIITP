import re
import random

KEYWORDS = {'if', 'else', 'while', 'return', 'int', 'float', 'char'}
regex_patterns = {
    'KEYWORD': re.compile(r'\b(?:if|else|while|return|int|float|char)\b'),
    'IDENTIFIER': re.compile(r'\b[a-zA-Z_][a-zA-Z0-9_]*\b'),
    'FLOAT': re.compile(
        r'\b\d+\.\d+\b'),  # Moved FLOAT before INTEGER to avoid conflicts
    'INTEGER': re.compile(r'\b\d+\b'),
    'STRING': re.compile(r'"[^"]*"'),
    'CHARACTER': re.compile(r"'[^']'"),
    'OPERATOR': re.compile(r'[+\-*/%==!=<>]=?|&&|\|\|'),
    'DELIMITER': re.compile(r'[;,{}()]')
}

symbol_table, ERRORS = {}, []


def add_to_symbol_table(identifier, data_type, line_number):
    if identifier not in symbol_table:
        symbol_table[identifier] = {
            'data_type': data_type,
            'memory_location': hex(random.randint(0x1000000, 0xFFFFFFF)),
            'line_number': line_number
        }
    elif symbol_table[identifier][
            'data_type'] == 'unknown' and data_type != 'unknown':
        symbol_table[identifier]['data_type'] = data_type


def lex(source_code):
    tokens, line_number, in_multiline_comment = [], 1, False

    for line in source_code.split('\n'):
        line = re.sub(r'//.*$', '', line)  # Remove single-line comments

        if '/*' in line:
            in_multiline_comment = True  # Mark that a multi-line comment started
            line = line.split('/')[0]  # Keep only the part before '/'

        if '*/' in line and in_multiline_comment:
            in_multiline_comment = False
            line = line.split('/')[1]  # Resume processing after '/'

        if in_multiline_comment:
            line_number += 1  # Continue counting lines but don't skip the whole line
            continue

        pos = 0
        while pos < len(line):
            match = next((pattern.match(line, pos)
                          for _, pattern in regex_patterns.items()
                          if pattern.match(line, pos)), None)
            if match:
                token_value = match.group(0)
                token_type = next(k for k, v in regex_patterns.items()
                                  if v.match(token_value))

                if token_type == 'KEYWORD' and token_value in {
                        'int', 'float', 'char'
                }:
                    remaining_line = line[pos + len(token_value):].strip()
                    next_token = remaining_line.split(
                    )[0] if remaining_line else None
                    if next_token:
                        add_to_symbol_table(next_token, token_value,
                                            line_number)

                elif token_type == 'IDENTIFIER' and token_value not in KEYWORDS:
                    add_to_symbol_table(token_value, 'unknown', line_number)

                tokens.append((token_type, token_value))
                pos = match.end()
            else:
                if not line[pos].isspace():
                    ERRORS.append(
                        f"Illegal character '{line[pos]}' at line {line_number}"
                    )
                pos += 1

        line_number += 1

    return tokens


def check_errors(source_code):
    if any(lit == "" for lit in re.findall(r'"(.*?)"', source_code)):
        ERRORS.append("Unterminated string literal found.")
    if '/' in source_code and '/' not in source_code:
        ERRORS.append("Unterminated multi-line comment found.")


source_code = input("Enter C code: ")
check_errors(source_code)
tokens = lex(source_code)

print("\nTokens:", tokens)
print("\nSymbol Table:")
for identifier, details in symbol_table.items():
    print(
        f"Identifier: {identifier}, Type: {details['data_type']}, Memory Location: {details['memory_location']}, Line Number: {details['line_number']}"
    )

print("\nErrors:", ERRORS)