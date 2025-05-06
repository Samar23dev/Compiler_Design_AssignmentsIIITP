def PDA():
    s=input("Enter String for Given CFG{0,1} :")
    n=len(s)
    stack=[]
    state=1
    i=0
    if (len(s)==0):
        state="qf"
    while(i<n and state==1):
        if (s[i]=='0'):
            stack.append(s[i])
        else:
            state=2
            break
        i+=1

    while(i<n and state==2 and len(stack)!=0):
        if (s[i]=='1'):
            stack.pop()
            if (i==n-1 and len(stack)==0):
                state="qf"
                break
        else:
            break
        i+=1    

    if (state=="qf"):
        print("Given CFG is accepted by PDA",s," : ",state)
    else:
        print("CFG is rejected by PDA at state ",s," : ",state)
        
PDA()