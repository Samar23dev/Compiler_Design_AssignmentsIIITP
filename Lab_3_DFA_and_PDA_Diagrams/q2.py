def PDA():
    string = input("Enter any string over given alphabet{0,1} : ")
    n=len(string)
    if (n==0):
        print("Empty String \u03B5")
        return None
    stack,state,flag=[],0,True
    for i in string:
        if state==0:
            if i=='0' or i=='1': stack.append(i)
            elif i=='C' or i=='c':
                state=1
                continue
        elif state==1:
            if (len(stack)>0 and i==stack[-1]): stack.pop()
            else:
                flag=False
                break

    if (len(stack)==0 and flag==True):
        state=2
    if (len(stack)>0):
            print("Stack top : ",stack[-1])
    else:
            print("Stack top : ","Empty")
    if (state==2):
        print("String is accepted at state : ",state)
    else:
        print("String is rejected at state : ",state)

PDA()
while True:
    print("samar")