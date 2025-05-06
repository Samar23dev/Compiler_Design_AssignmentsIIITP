import re
def tokenizer(s):
    keywords = {'int', 'float', 'char', 'if', 'else', 'while', 'for'}
    operators = {'+', '-', '*', '/', '=', '==', '++', '--', '%', '&&', '||', '!', '>', '<', '>=', '<='}
    isidentifiers = r'[_a-zA-Z][_a-zA-Z0-9]*'
    isdelimiter = r'[;,(){}]'
    isoperator = r'[&*^%+-=]+'
    isnum = r'\b\d+\b'
    identifier_limit = 31
    
    s = re.sub(r'//.*', '', s)
    s = re.sub(r'/\*.*?\*/', '', s, flags=re.DOTALL)
    s = re.sub(r'\s+', ' ', s).strip()
    
    x = re.findall(isidentifiers, s)
    keylist = [i for i in x if i in keywords]
    print("keywords are ", keylist)
    
    idlist = []
    for i in x:
        if i not in keywords:
            if len(i) > identifier_limit:
                temp=i[:identifier_limit]
                print("Identifier limit reached (trucated) ",temp)
                idlist.append(temp)
            else:
                idlist.append(i)
    print("Identifiers are ", idlist)
    
    y = re.findall(isnum, s)
    z = re.findall(isoperator, s)
    print(z)
    oplist = [i for i in z if i in operators]
    t = re.findall(isdelimiter, s)
    
    print("Numbers : ", y)
    print("Operators : ", oplist)
    print("Delimiters : ", t)

s = input("Enter statement : ")
s='''/* This is a test */
int a = 5;
if (a &gt; 3) { // Check condition
a++;
}'''
tokenizer(s)