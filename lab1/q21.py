def DFA2():
     s=input("Enter String over given Alphabet{0,1} : ")
     if (len(s)==0):
          print("Empty String ")
          return None
     state=0
     for i in range(0,len(s)):
          if (s[i]=='0'):
               if (state==3):
                    break
               else:
                    state+=1
          else:
               state=0
          if state == 3:
            break
     print("String ended at State : ",state)
     if (state==3):
          print("String is rejected")
     else:
          print("String is accepted")
               
        
DFA2()