import copy

# Perform grammar augmentation
def grammarAugmentation(rules, nonterm_userdef, start_symbol):
    # newRules stores processed output rules
    newRules = []

    # Create unique 'symbol' to represent new start symbol
    newChar = start_symbol + "'"
    while (newChar in nonterm_userdef):
        newChar += "'"

    # Adding rule to bring start symbol to RHS
    newRules.append([newChar, ['.', start_symbol]])

    # New format => [LHS,[.RHS]]
    for rule in rules:
        # Split LHS from RHS
        k = rule.split("->")
        lhs = k[0].strip()
        rhs = k[1].strip()
        
        # Split all rule at '|'
        multirhs = rhs.split('|')
        for rhs1 in multirhs:
            rhs1 = rhs1.strip().split()
            
            # ADD dot pointer at start of RHS
            rhs1.insert(0, '.')
            newRules.append([lhs, rhs1])
    return newRules

# Find closure
def findClosure(input_state, dotSymbol):
    global start_symbol, separatedRulesList, statesDict

    # closureSet stores processed output
    closureSet = []

    # If findClosure is called for I0
    if dotSymbol == start_symbol:
        for rule in separatedRulesList:
            if rule[0] == dotSymbol:
                closureSet.append(rule)
    else:
        # For any higher state than I0
        closureSet = input_state

    # Iterate till new states are getting added in closureSet
    prevLen = -1
    while prevLen != len(closureSet):
        prevLen = len(closureSet)
        tempClosureSet = []

        # If dot pointing at new symbol, add corresponding rules to tempClosure
        for rule in closureSet:
            indexOfDot = rule[1].index('.')
            if rule[1][-1] != '.':
                dotPointsHere = rule[1][indexOfDot + 1]
                for in_rule in separatedRulesList:
                    if dotPointsHere == in_rule[0] and in_rule not in tempClosureSet:
                        tempClosureSet.append(in_rule)

        # Add new closure rules to closureSet
        for rule in tempClosureSet:
            if rule not in closureSet:
                closureSet.append(rule)
    return closureSet

def compute_GOTO(state):
    global statesDict, stateCount, stateMap

    # Find all symbols on which we need to make function call - GOTO
    generateStatesFor = []
    for rule in statesDict[state]:
        # If rule is not "Handle"
        if rule[1][-1] != '.':
            indexOfDot = rule[1].index('.')
            dotPointsHere = rule[1][indexOfDot + 1]
            if dotPointsHere not in generateStatesFor:
                generateStatesFor.append(dotPointsHere)

    # Call GOTO iteratively on all symbols pointed by dot
    if len(generateStatesFor) != 0:
        for symbol in generateStatesFor:
            GOTO(state, symbol)
    return

def GOTO(state, charNextToDot):
    global statesDict, stateCount, stateMap

    # newState - stores processed new state
    newState = []
    for rule in statesDict[state]:
        indexOfDot = rule[1].index('.')
        if rule[1][-1] != '.':
            if rule[1][indexOfDot + 1] == charNextToDot:
                # Swapping element with dot to perform shift operation
                shiftedRule = copy.deepcopy(rule)
                shiftedRule[1][indexOfDot] = shiftedRule[1][indexOfDot + 1]
                shiftedRule[1][indexOfDot + 1] = '.'
                newState.append(shiftedRule)

    # Add closure rules for newState
    addClosureRules = []
    for rule in newState:
        indexDot = rule[1].index('.')
        # Check that rule is not "Handle"
        if rule[1][-1] != '.':
            closureRes = findClosure(newState, rule[1][indexDot + 1])
            for rule in closureRes:
                if rule not in addClosureRules and rule not in newState:
                    addClosureRules.append(rule)

    # Add closure result to newState
    for rule in addClosureRules:
        newState.append(rule)

    # Find if newState already present in Dictionary
    stateExists = -1
    for state_num in statesDict:
        if statesDict[state_num] == newState:
            stateExists = state_num
            break

    # stateMap is a mapping of GOTO with its output states
    if stateExists == -1:
        # If newState is not in dictionary, then create new state
        stateCount += 1
        statesDict[stateCount] = newState
        stateMap[(state, charNextToDot)] = stateCount
    else:
        # If state repetition found, assign that previous state number
        stateMap[(state, charNextToDot)] = stateExists
    return

def generateStates(statesDict):
    prev_len = -1
    called_GOTO_on = []

    # Run loop till new states are getting added
    while (len(statesDict) != prev_len):
        prev_len = len(statesDict)
        keys = list(statesDict.keys())

        # Make compute_GOTO function call on all states in dictionary
        for key in keys:
            if key not in called_GOTO_on:
                called_GOTO_on.append(key)
                compute_GOTO(key)
    return

# Calculation of first (epsilon is denoted by '#')
def first(rule):
    global rules, nonterm_userdef, term_userdef, diction, firsts
    
    # Recursion base condition (for terminal or epsilon)
    if len(rule) != 0 and (rule is not None):
        if rule[0] in term_userdef:
            return rule[0]
        elif rule[0] == '#':
            return '#'

    # Condition for Non-Terminals
    if len(rule) != 0:
        if rule[0] in list(diction.keys()):
            # fres temporary list of result
            fres = []
            rhs_rules = diction[rule[0]]
            
            # Call first on each rule of RHS fetched (& take union)
            for itr in rhs_rules:
                indivRes = first(itr)
                if type(indivRes) is list:
                    for i in indivRes:
                        fres.append(i)
                else:
                    fres.append(indivRes)

            # If no epsilon in result received return fres
            if '#' not in fres:
                return fres
            else:
                # Apply epsilon rule => f(ABC)=f(A)-{e} U f(BC)
                newList = []
                fres.remove('#')
                if len(rule) > 1:
                    ansNew = first(rule[1:])
                    if ansNew != None:
                        if type(ansNew) is list:
                            newList = fres + ansNew
                        else:
                            newList = fres + [ansNew]
                    else:
                        newList = fres
                    return newList
                
                # If epsilon still persists - keep it in result of first
                fres.append('#')
                return fres

# Calculation of follow
def follow(nt):
    global start_symbol, rules, nonterm_userdef, term_userdef, diction, firsts, follows
    
    # For start symbol return $ (recursion base case)
    solset = set()
    if nt == start_symbol:
        solset.add('$')

    # Check all occurrences
    for curNT in diction:
        rhs = diction[curNT]
        
        # Go for all productions of NT
        for subrule in rhs:
            if nt in subrule:
                # Call for all occurrences on non-terminal in subrule
                while nt in subrule:
                    index_nt = subrule.index(nt)
                    subrule = subrule[index_nt + 1:]
                    
                    # Empty condition - call follow on LHS
                    if len(subrule) != 0:
                        # Compute first if symbols on RHS of target Non-Terminal exists
                        res = first(subrule)
                        
                        # If epsilon in result apply rule
                        if '#' in res:
                            newList = []
                            res.remove('#')
                            ansNew = follow(curNT)
                            if ansNew != None:
                                if type(ansNew) is list:
                                    newList = res + ansNew
                                else:
                                    newList = res + [ansNew]
                            else:
                                newList = res
                            res = newList
                    else:
                        # When nothing in RHS, go circular and take follow of LHS
                        if nt != curNT:
                            res = follow(curNT)

                    # Add follow result in set form
                    if res is not None:
                        if type(res) is list:
                            for g in res:
                                solset.add(g)
                        else:
                            solset.add(res)
    return list(solset)

def createParseTable(statesDict, stateMap, T, NT):
    global separatedRulesList, diction, parseTable

    # Create rows and cols
    rows = list(statesDict.keys())
    cols = T+['$']+NT

    # Create empty table
    parseTable = {}
    for i in rows:
        parseTable[i] = {}
        for j in cols:
            parseTable[i][j] = ''

    # Make shift and GOTO entries in table
    for entry in stateMap:
        state = entry[0]
        symbol = entry[1]
        if symbol in NT:
            parseTable[state][symbol] = stateMap[entry]
        elif symbol in T:
            parseTable[state][symbol] = f"S{stateMap[entry]}"

    # Start REDUCE procedure
    # Number the separated rules
    numbered = {}
    key_count = 0
    for rule in separatedRulesList:
        tempRule = copy.deepcopy(rule)
        tempRule[1].remove('.')
        numbered[key_count] = tempRule
        key_count += 1

    # Start REDUCE procedure
    # Format for follow computation
    addedR = f"{separatedRulesList[0][0]} -> {separatedRulesList[0][1][1]}"
    rules.insert(0, addedR)
    for rule in rules:
        k = rule.split("->")
        
        # Remove un-necessary spaces
        k[0] = k[0].strip()
        k[1] = k[1].strip()
        rhs = k[1]
        multirhs = rhs.split('|')
        
        # Remove un-necessary spaces
        for i in range(len(multirhs)):
            multirhs[i] = multirhs[i].strip()
            multirhs[i] = multirhs[i].split()
        diction[k[0]] = multirhs

    # Find 'handle' items and calculate follow
    for stateno in statesDict:
        for rule in statesDict[stateno]:
            if rule[1][-1] == '.':
                # Match the item
                temp2 = copy.deepcopy(rule)
                temp2[1].remove('.')
                for key in numbered:
                    if numbered[key] == temp2:
                        # Put Rn in ACTION symbol columns in follow of LHS
                        follow_result = follow(rule[0])
                        for col in follow_result:
                            if key == 0:
                                parseTable[stateno][col] = "Accept"
                            else:
                                if parseTable[stateno][col] and parseTable[stateno][col] != "Accept":
                                    parseTable[stateno][col] += f"|R{key}"
                                else:
                                    parseTable[stateno][col] = f"R{key}"

    # Print table
    print("\nSLR(1) parsing table:\n")
    print(" " * 9, end="")
    for col in cols:
        print(f"{col:^8}", end="")
    print()
    print()
    
    for state in parseTable:
        print(f" I{state:<8}", end="")
        for col in cols:
            print(f"{parseTable[state].get(col, ''):^8}", end="")
        print()

def printResult(rules):
    for rule in rules:
        print(f"{rule[0]} -> {' '.join(rule[1])}")


def parse_input(input_string, term_userdef):
    global parseTable
    
    # Add $ to input
    input_string = input_string + "$"
    input_tokens = list(input_string)
    
    # Initialize stack with 0
    stack = [0]
    input_ptr = 0
    
    print(f"\nParsing Input: {input_string[:-1]}\n")
    print("-" * 80)
    print(f"|{'Step':^15}|{'Stack':^20}|{'Input':^20}|{'Action':^18}|")
    print("-" * 80)
    
    step = 1
    try:
        while True:
            current_state = stack[-1]
            current_symbol = input_tokens[input_ptr]
            
            if current_symbol not in term_userdef and current_symbol != '$':
                raise Exception(f"Error: Symbol '{current_symbol}' not in grammar terminals")
            
            action = parseTable[current_state].get(current_symbol, '')
            
            if not action:
                raise Exception(f"Error: No action defined for state {current_state} and symbol '{current_symbol}'")
            
            stack_str = " ".join(str(s) for s in stack)
            input_str = "".join(input_tokens[input_ptr:])
            
            # Handle multiple actions (shift/reduce conflicts)
            if '|' in action:
                # For simplicity, just take the first action (prefer shift)
                if 'S' in action:
                    action = next(a for a in action.split('|') if a.startswith('S'))
                else:
                    action = action.split('|')[0]
            
            if action.startswith('S'):
                # Shift action
                next_state = int(action[1:])
                print(f"|{step:^15}|{stack_str:^20}|{input_str:^20}|{action:^18}|")
                stack.append(current_symbol)
                stack.append(next_state)
                input_ptr += 1
            
            elif action.startswith('R'):
                # Reduce action
                rule_num = int(action[1:])
                lhs, rhs = separatedRulesList[rule_num]
                rhs = [r for r in rhs if r != '.']  # Remove the dot
                
                # Pop 2 * len(rhs) elements from stack
                for _ in range(2 * len(rhs)):
                    stack.pop()
                
                # Get state at top of stack and push LHS and new state
                prev_state = stack[-1]
                goto = parseTable[prev_state].get(lhs, '')
                
                if not goto:
                    raise Exception(f"Error: No GOTO defined for state {prev_state} and non-terminal '{lhs}'")
                
                print(f"|{step:<15}|{stack_str:^20}|{input_str:^20}|{action:^18}|")
                stack.append(lhs)
                stack.append(goto)
            
            elif action == "Accept":
                print(f"|{step:^15}|{stack_str:^20}|{input_str:^20}|{'Accept':^18}|")
                print("-" * 80)
                print(f"\nInput string '{input_string[:-1]}' accepted!")
                return True
            
            step += 1
            
    except Exception as e:
        print(f"|{step:^15}|{stack_str:^20}|{input_str:^20}|{' ':^18}|")
        print("-" * 80)
        print(e)
        print(f"Input string '{input_string[:-1]}' is not valid according to the grammar")
        return False

# Main function to run the parser
def main():
    global rules, nonterm_userdef, term_userdef, start_symbol
    global separatedRulesList, diction, statesDict, stateMap, stateCount, parseTable
    
    rules = ["S -> C C", "C -> c C | d"]
    nonterm_userdef = ['S', 'C']
    term_userdef = ['c', 'd']
    start_symbol = nonterm_userdef[0]
   
    
    # Print original grammar
    print("\nOriginal grammar input:\n")
    for y in rules:
        print(y)
    
    # Augment grammar and print
    print("\nGrammar after Augmentation: \n")
    separatedRulesList = grammarAugmentation(rules, nonterm_userdef, start_symbol)
    printResult(separatedRulesList)
    
    # Calculate closure
    start_symbol = separatedRulesList[0][0]
    print("\nCalculated closure: I0\n")
    I0 = findClosure(0, start_symbol)
    printResult(I0)
    
    # Initialize global variables
    statesDict = {}
    stateMap = {}
    diction = {}
    firsts = {}
    follows = {}
    
    # Add first state and generate all states
    statesDict[0] = I0
    stateCount = 0
    generateStates(statesDict)
    
    # Print generated states
    print("\nStates Generated: \n")
    for st in statesDict:
        print(f"State = I{st}")
        printResult(statesDict[st])
        print()

    # Create parse table
    parseTable = {}
    createParseTable(statesDict, stateMap, term_userdef, nonterm_userdef)
    
    # Test with input strings
    print("\n==================================================\n")
    print("Testing String 1 : \n")
    parse_input("cdd", term_userdef)
    
    print("\n==================================================\n")
    print("Testing String 2 : \n")
    parse_input("ccc", term_userdef)

if __name__ == "__main__":
    main()