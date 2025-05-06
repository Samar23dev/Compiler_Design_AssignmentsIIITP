def DFA():
    string =input("Enter String over alphabet{0-9} : ")
    state=0
    n=len(string)
    if (n==0):
        print("Empty String \u03B5")
        return None
    mod_0=['0','3','6','9']
    mod_1=['1','4','7']
    mod_2=['2','5','8']
    for i in string:
        if (state==0):
            if i in mod_0: state=0
            elif i in mod_1: state=1
            elif i in mod_2: state=2
        elif (state==1):
            if i in mod_0: state=1
            elif i in mod_1: state=2
            elif i in mod_2: state=0
        elif (state==2):
            if i in mod_0: state=2
            elif i in mod_1: state=0
            elif i in mod_2: state=1
    
    if (state==0):
        print("Given string is accepted at state : ",state)
    else:
        print("Given string is rejected at state : ",state)
    
DFA()