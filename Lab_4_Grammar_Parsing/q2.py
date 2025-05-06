import re
def tokenizer(s):
    kw = {'int', 'float', 'char', 'if', 'else', 'while', 'for'}
    op = {'+', '-', '*', '/', '=', '==', '++', '--', '%', '&&', '||', '!', '>', '<', '>=', '<='}
    dl = {';', ',', '(', ')', '{', '}'}
    id_limit = 31
    id=r'[_a-zA-Z]\s*'
    num=r'\b\d+\b'
    
    s = re.sub(r'//.*', '', s)
    s = re.sub(r'/\*.*?\*/', '', s, flags=re.DOTALL)
    s = re.sub(r'\s+', ' ', s).strip()
    
    tokens = re.findall(r'==|!=|<=|>=|\+\+|--|[+\-*/%=&|!<>]=?|[;,(){}]|\b\d+\b|[_a-zA-Z][_a-zA-Z0-9]*', s)
    
    for tok in tokens:
        if tok in kw:
            print("Keyword:", tok)
        elif re.match(id, tok) != None:
            if len(tok) > id_limit:
                print("Warning!!!!")
                print("Identifier:", tok[:id_limit], "(truncated)")
            else:
                print("Identifier:", tok)
        elif re.match(num, tok) != None:
            print("Number:", tok)
        elif tok in op:
            print("Operator:", tok)
        elif tok in dl:
            print("Delimiter:", tok)
        else:
            print("Unrecognized token:", tok)

# Example usage
s=input("Enter string : ")
tokenizer(s)
# s0="int x= 42;"
# s1="float y = x + 5;"
# s2 = '''/* This is a test */
# int a = 5;
# if (a > 3) { // Check condition
# a++;
# }'''
# s3="int this_is_a_very_long_identifier_name_that_needs_truncation = 10;"
# print("TEST CASE 1 OUTPUT ----------------------")
# tokenizer(s0)
# print("TEST CASE 2 OUTPUT---------------------------")
# tokenizer(s1)
# print("TEST CASE 3 OUTPUT-----------------------------------")
# tokenizer(s2)
# print("TEST CASE 4 OUTPUT-----------------------------------")
# tokenizer(s3)
