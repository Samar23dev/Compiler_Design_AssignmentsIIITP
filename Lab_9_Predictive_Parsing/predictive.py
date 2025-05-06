grammar_rules = [
    ("E", ["T","G"]), 
    ("G", ["+","T","G"]), 
    ("G", ["#"]),
    ("T", ["F","H"]), 
    ("H", [ "*", "F",'H']), 
    ("H", [ "#"]), 
    ("F", ["(", "E", ")"]), 
    ("F", ["id"])
]

terminals = {"id", "+", "*", "(", ")", "$"}
non_terminals = {"E",'G','H', "T", "F"}
transformed_grammar = []
first_sets, follow_sets, parsing_table = {}, {}, {}

def remove_left_recursion():
    global non_terminals, transformed_grammar
    new_grammar, new_non_terminals = [], set(non_terminals)
    
    for non_terminal in non_terminals:
        direct_recursions, other_productions = [], []
        for rule in grammar_rules:
            if rule[0] == non_terminal:
                (direct_recursions if rule[1] and rule[1][0] == non_terminal else other_productions).append(
                    rule[1][1:] if rule[1] and rule[1][0] == non_terminal else rule[1]
                )
        
        if not direct_recursions:
            [new_grammar.append((non_terminal, production)) for production in other_productions]
            continue
        
        new_non_terminal = non_terminal + "'"
        new_non_terminals.add(new_non_terminal)
        [new_grammar.append((non_terminal, production + [new_non_terminal])) for production in other_productions]
        [new_grammar.append((new_non_terminal, recursion + [new_non_terminal])) for recursion in direct_recursions]
        new_grammar.append((new_non_terminal, ["#"]))
    
    transformed_grammar.extend(new_grammar)
    non_terminals = new_non_terminals
    print("Grammar after removing left recursion:")
    for rule in transformed_grammar:
        print(f"{rule[0]} → {' '.join(rule[1])}")
    print()

def remove_left_factoring():
    global non_terminals, transformed_grammar
    new_grammar = []
    
    for non_terminal in non_terminals:
        productions = [rule[1] for rule in transformed_grammar if rule[0] == non_terminal]
        i = 0
        while i < len(productions):
            for j in range(i + 1, len(productions)):
                if productions[i] and productions[j] and productions[i][0] == productions[j][0]:
                    new_non_terminal = f"{non_terminal}_{len(new_grammar)}"
                    non_terminals.add(new_non_terminal)
                    new_grammar.append((non_terminal, [productions[i][0], new_non_terminal]))
                    new_grammar.append((new_non_terminal, productions[i][1:] or ["#"]))
                    new_grammar.append((new_non_terminal, productions[j][1:] or ["#"]))
                    productions.pop(j)
                    productions.pop(i)
                    i -= 1
                    break
            i += 1
        [new_grammar.append((non_terminal, production)) for production in productions]
    
    transformed_grammar.clear()
    transformed_grammar.extend(new_grammar)
    print("Grammar after removing left factoring:")
    for rule in transformed_grammar:
        print(f"{rule[0]} → {' '.join(rule[1])}")
    print()

def compute_first_sets():
    for symbol in terminals | non_terminals:
        first_sets[symbol] = set()
    for terminal in terminals:
        if terminal != "$":
            first_sets[terminal].add(terminal)
    
    changed = True
    while changed:
        changed = False
        for left_side, right_side in transformed_grammar:
            original_size = len(first_sets[left_side])
            if right_side[0] == "#":
                first_sets[left_side].add("#")
            else:
                nullable = True
                for symbol in right_side:
                    if not nullable:
                        break
                    first_sets[left_side].update(s for s in first_sets[symbol] if s != "#")
                    nullable = "#" in first_sets[symbol]
                    if nullable and symbol == right_side[-1]:
                        first_sets[left_side].add("#")
            changed |= len(first_sets[left_side]) > original_size

def compute_follow_sets():
    for non_terminal in non_terminals:
        follow_sets.setdefault(non_terminal, set())
    follow_sets["E"].add("$")

    changed = True
    while changed:
        changed = False
        for left_side, right_side in transformed_grammar:
            for index, symbol in enumerate(right_side):
                if symbol in non_terminals:
                    original_size = len(follow_sets[symbol])
                    nullable = True
                    for next_symbol_index in range(index + 1, len(right_side)):
                        if not nullable:
                            break
                        follow_sets[symbol].update(first_sets[right_side[next_symbol_index]] - {"#"})
                        nullable = "#" in first_sets[right_side[next_symbol_index]]
                    if nullable or index == len(right_side) - 1:
                        follow_sets[symbol].update(follow_sets[left_side])
                    changed |= len(follow_sets[symbol]) > original_size

def construct_parsing_table():
    for left_side, right_side in transformed_grammar:
        if right_side == ["#"]:
            first_production = {"#"}
        else:
            first_production = set().union(
                *(first_sets[right_side[i]] - {"#"} for i in range(len(right_side)) if all("#" in first_sets[right_side[j]] for j in range(i)))
            )
            if all("#" in first_sets[symbol] for symbol in right_side if symbol != "#"):
                first_production.add("#")
        
        for terminal in first_production - {"#"}:
            parsing_table[(left_side, terminal)] = right_side
        if right_side == ["#"]:
            for terminal in follow_sets[left_side]:
                parsing_table[(left_side, terminal)] = right_side

def print_sets():
    print("FIRST Sets:")
    for non_terminal in non_terminals:
        print(f"{non_terminal}: {{ {' '.join(sorted(first_sets[non_terminal]))} }}")
    print("\nFOLLOW Sets:")
    for non_terminal in non_terminals:
        print(f"{non_terminal}: {{ {' '.join(sorted(follow_sets[non_terminal]))} }}")
    print()

def print_parsing_table():
    print("Predictive Parsing Table:\n")
    header = ["NT/T"] + list(terminals)
    row_format = "{:<12}" * len(header)
    print(row_format.format(*header))
    print("-" * (12 * len(header)))
    
    for non_terminal in non_terminals:
        row = [non_terminal]
        for terminal in terminals:
            row.append(f"{non_terminal} → {' '.join(parsing_table[non_terminal, terminal])}" if (non_terminal, terminal) in parsing_table else "")
        print(row_format.format(*row))
        print("-" * (12 * len(header)))

def parse_input_string(input_string):
    input_string += "$"
    parsing_stack = ["$", "E"]
    input_index = 0
    print(f"Parsing: {input_string[:-1]}\n")
    print(f"{'Stack':<30}{'Input':<20}{'Action'}")
    print("=" * 70)

    while parsing_stack:
        top_of_stack, current_input_symbol = parsing_stack[-1], "id" if input_string[input_index:].startswith("id") else input_string[input_index]
        print(f"{' '.join(parsing_stack):<30}{input_string[input_index:]:<20}", end="")

        if top_of_stack in terminals and top_of_stack == current_input_symbol:
            parsing_stack.pop()
            input_index += 2 if top_of_stack == "id" else 1
            print(f"Match {top_of_stack}")
        elif top_of_stack == "#":
            parsing_stack.pop()
            print("Pop #")
        elif top_of_stack in non_terminals and (top_of_stack, current_input_symbol) in parsing_table:
            production = parsing_table[(top_of_stack, current_input_symbol)]
            parsing_stack.pop()
            if production[0] != "#":
                for symbol in reversed(production):
                    parsing_stack.append(symbol)
            print(f"{top_of_stack} → {' '.join(production)}")
        else:
            print(f"Error: No entry for ({top_of_stack}, {current_input_symbol})")
            return False
    
    return input_index == len(input_string)

print("Original Grammar:")
for rule in grammar_rules:
    print(f"{rule[0]} → {' '.join(rule[1])}")
print()

remove_left_recursion()
remove_left_factoring()
compute_first_sets()
compute_follow_sets()
construct_parsing_table()
print_sets()
print_parsing_table()

for test_string in ["id+id*id", "id+*id"]:
    print(f"\nInput '{test_string}' is {'accepted' if parse_input_string(test_string) else 'not accepted'}")
    print("-" * 50)


# grammar = [
#     ("E", ["E", "+", "T"]), 
#     ("E", ["T"]), 
#     ("T", ["T", "*", "F"]), 
#     ("T", ["F"]), 
#     ("F", ["(", "E", ")"]), 
#     ("F", ["id"])
# ]

# t, n = {"id", "+", "*", "(", ")", "$"}, {"E", "T", "F"}
# tg, fs, fls, pt = [], {}, {}, {}

# def rlr():
#     global n, tg
#     ng, nn = [], set(n)
    
#     for a in n:
#         al, be = [], []
#         for p in grammar:
#             if p[0] == a:
#                 (al if p[1] and p[1][0] == a else be).append(p[1][1:] if p[1] and p[1][0] == a else p[1])
        
#         if not al:
#             [ng.append((a, b)) for b in be]
#             continue
        
#         ap = a + "'"
#         nn.add(ap)
#         [ng.append((a, b + [ap])) for b in be]
#         [ng.append((ap, alr + [ap])) for alr in al]
#         ng.append((ap, ["#"]))
    
#     tg.extend(ng)
#     n = nn
#     print("Grammar after removing left recursion:")
#     for p in tg:
#         print(f"{p[0]} → {' '.join(p[1])}")
#     print()

# def rlf():
#     global n, tg
#     ng = []
    
#     for nt in n:
#         pr = [p[1] for p in tg if p[0] == nt]
#         i = 0
#         while i < len(pr):
#             for j in range(i + 1, len(pr)):
#                 if pr[i] and pr[j] and pr[i][0] == pr[j][0]:
#                     nnt = f"{nt}_{len(ng)}"
#                     n.add(nnt)
#                     ng.append((nt, [pr[i][0], nnt]))
#                     ng.append((nnt, pr[i][1:] or ["#"]))
#                     ng.append((nnt, pr[j][1:] or ["#"]))
#                     pr.pop(j)
#                     pr.pop(i)
#                     i -= 1
#                     break
#             i += 1
#         [ng.append((nt, p)) for p in pr]
    
#     tg.clear()
#     tg.extend(ng)
#     print("Grammar after removing left factoring:")
#     for p in tg:
#         print(f"{p[0]} → {' '.join(p[1])}")
#     print()

# def cf():
#     for x in t | n:
#         fs[x] = set()
#     for t_sym in t:
#         if t_sym != "$":
#             fs[t_sym].add(t_sym)
    
#     c = 1
#     while c:
#         c = 0
#         for l, r in tg:
#             ol = len(fs[l])
#             if r[0] == "#":
#                 fs[l].add("#")
#             else:
#                 ae = 1
#                 for i in range(len(r)):
#                     if not ae:
#                         break
#                     fs[l].update(s for s in fs[r[i]] if s != "#")
#                     ae = "#" in fs[r[i]]
#                     if ae and i == len(r) - 1:
#                         fs[l].add("#")
#             c |= len(fs[l]) > ol

# def cfl():
#     for nt in n:
#         fls.setdefault(nt, set())
#     fls["E"].add("$")

#     c = 1
#     while c:
#         c = 0
#         for l, r in tg:
#             for i, s in enumerate(r):
#                 if s in n:
#                     ol = len(fls[s])
#                     ae = 1
#                     for j in range(i + 1, len(r)):
#                         if not ae:
#                             break
#                         fls[s].update(fs[r[j]] - {"#"})
#                         ae = "#" in fs[r[j]]
#                     if ae or i == len(r) - 1:
#                         fls[s].update(fls[l])
#                     c |= len(fls[s]) > ol

# def cpt():
#     for l, r in tg:
#         if r == ["#"]:
#             fp = {"#"}
#         else:
#             fp = set().union(*(fs[r[i]] - {"#"} for i in range(len(r)) if all("#" in fs[r[j]] for j in range(i))))
#             if all("#" in fs[ri] for ri in r if ri != "#"):
#                 fp.add("#")
        
#         for a in fp - {"#"}:
#             pt[(l, a)] = r
#         if r == ["#"]:
#             for b in fls[l]:
#                 pt[(l, b)] = r

# def ps():
#     print("FIRST Sets:")
#     for nt in n:
#         print(f"{nt}: {{ {' '.join(sorted(fs[nt]))} }}")
#     print("\nFOLLOW Sets:")
#     for nt in n:
#         print(f"{nt}: {{ {' '.join(sorted(fls[nt]))} }}")
#     print()

# def ppt():
#     print("Predictive Parsing Table:\n")
#     header = ["NT/T"] + list(t)
#     row_format = "{:<12}" * len(header)
#     print(row_format.format(*header))
#     print("-" * (12 * len(header)))
    
#     for nt in n:
#         row = [nt]
#         for tm in t:
#             row.append(f"{nt} → {' '.join(pt[nt, tm])}" if (nt, tm) in pt else "")
#         print(row_format.format(*row))
#         print("-" * (12 * len(header)))

# def pp(ipt):
#     ipt += "$"
#     stk = ["$", "E"]
#     idx = 0
#     print(f"Parsing: {ipt[:-1]}\n")
#     print(f"{'Stack':<30}{'Input':<20}{'Action'}")
#     print("=" * 70)

#     while stk:
#         top, ci = stk[-1], "id" if ipt[idx:].startswith("id") else ipt[idx]
#         print(f"{' '.join(stk):<30}{ipt[idx:]:<20}", end="")

#         if top in t and top == ci:
#             stk.pop()
#             idx += 2 if top == "id" else 1
#             print(f"Match {top}")
#         elif top == "#":
#             stk.pop()
#             print("Pop #")
#         elif top in n and (top, ci) in pt:
#             pr = pt[(top, ci)]
#             stk.pop()
#             if pr[0] != "#":
#                 for s in reversed(pr):
#                     stk.append(s)
#             print(f"{top} → {' '.join(pr)}")
#         else:
#             print(f"Error: No entry for ({top}, {ci})")
#             return False
    
#     return idx == len(ipt)

# print("Original Grammar:")
# for p in grammar:
#     print(f"{p[0]} → {' '.join(p[1])}")
# print()

# rlr()
# rlf()
# cf()
# cfl()
# cpt()
# ps()
# ppt()

# for s in ["id+id*id", "id+*id"]:
#     print(f"\nInput '{s}' is {'accepted' if pp(s) else 'not accepted'}")
#     print("-" * 50)

