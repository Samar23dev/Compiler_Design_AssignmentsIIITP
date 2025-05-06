def pda2():
    string=input("Enter String for CFG over {0,1} : ")
    stack=[]
    state="q1"
    for item in string:
        if (item=='0'):
            if (len(stack)==0 or stack[-1]=='0'):
                stack.append('0')
            elif (stack[-1]=='1'):
                stack.pop()

        elif (item=="1"):
            if (len(stack)==0 or stack[-1]=='1'):
                stack.append('1')
            elif (stack[-1]=='0'):
                stack.pop()

    if (len(stack)==0):
        state="qf"
            
    if (state=="qf"):
        print(f"{string} is accepted  at state : ",state)
    else:
        print(f"{string} is rejected  at state : ",state)
            
pda2()