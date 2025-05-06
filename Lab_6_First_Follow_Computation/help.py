from collections import defaultdict

def find(grammar):
    first = defaultdict(set)

    def first_rec(sym):
        if sym in first and first[sym]:
            return first[sym]

        if sym not in grammar:  
            return {sym}

        result = set()
        for prods in grammar[sym]:
            if prods == "ε":  
                result.add("ε")
            else:
                empty = True  
                for i, part in enumerate(prods.split()): 
                    part_first = first_rec(part)
                    result.update(part_first - {"ε"})
                    if "ε" not in part_first:
                        empty = False
                        break

                if empty:
                    result.add("ε") 

        first[sym] = result
        return result

    for non_terminal in grammar:
        first_rec(non_terminal)

    return {k: first[k] for k in grammar}  


grammar = {
        "S": [" A "],
        "A": [" B C "],
        "B": [" x "," ε "],
        "C": [" y "," z "],
    }
for x,y in grammar.items():
    print(x,"\t",y)
first_sets = find(grammar)

for variable, first_set in first_sets.items():
    print(f"FIRST({variable}) = {first_set}")