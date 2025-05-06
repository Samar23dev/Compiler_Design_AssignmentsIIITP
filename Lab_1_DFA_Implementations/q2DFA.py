def dfa_checker(s):
     state=0
     for i in range(0,len(s)):
          if (s[i]=='0'):
               if (state==3):
                    break
               else:
                    state+=1
          else:
               state=0
     print("Current State : ",state)
     if (state==3):
          return False
     else:
          return True
               
        

if __name__=="__main__":
     for i in range(5):
        string=input("Enter string of  (0 and 1) to check : ")
        if (len(string)==0):
            print("Empty String ")
        elif (dfa_checker(string)):
            print("Above string is accepted")
        else:
            print("String is not accepted")