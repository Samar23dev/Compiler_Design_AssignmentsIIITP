def first(c, prods, fs):
    if c not in fs: fs[c] = set()
    if c.islower(): fs[c].add(c); return fs[c]
    for prod in prods.get(c, []):
        if prod == '#': fs[c].add('#')
        elif prod[0].islower(): fs[c].add(prod[0])
        else:
            for char in prod:
                res = first(char, prods, fs)
                fs[c].update(res - {'#'})
                if '#' not in res: break
                if char == prod[-1]: fs[c].add('#')
    return fs[c]

def follow(c, start, prods, fs, follows):
    if c not in follows: follows[c] = set()
    if c == start: follows[c].add('$')
    for head, rules in prods.items():
        for prod in rules:
            if c in prod:
                idx = prod.index(c)
                if idx == len(prod) - 1:
                    if head != c:
                        follows[c].update(follow(head, start, prods, fs, follows))
                else:
                    next_sym = prod[idx + 1]
                    next_first = first(next_sym, prods, fs)
                    follows[c].update(next_first - {'#'})
                    if '#' in next_first:
                        follows[c].update(follow(head, start, prods, fs, follows))
    return follows[c]

def main():
    # prods = {'S': ['AaAb', 'BbBa'], 'A': ['#'], 'B': ['#']}
    # start = 'S'
    prods={
        'E':['TG'],
        'G':['+TG','#'],
        "T":['FH'],
        'H' : ["*FH",'#'],
        'F' : ["(E)",'id']
    }
    start='E'
    print("Grammar:")
    first_sets, follow_sets = {}, {}
    for nt, rules in prods.items():
        print(f"{nt} -> {' | '.join(rules)}")
    for nt in prods: first(nt, prods, first_sets)
    for nt in prods: follow(nt, start, prods, first_sets, follow_sets)
    
    print("\nFirst Sets:")
    for nt, fs in first_sets.items():
        if nt.isupper(): print(f"First({nt}) = {fs}")
    
    print("\nFollow Sets:")
    for nt, fs in follow_sets.items():
        print(f"Follow({nt}) = {fs}")

if __name__ == "__main__": main()
