def DFA():
     s=input("Enter String over given Alphabet{0,1} : ")
     if (len(s)==0):
          print("Empty String ")
          return None
     state=0
     for i in range(0,len(s)):
          if (s[i]=='0'):
               if (state==3):
                    state=3
               else:
                    state+=1
          else:
               state=0
          if state == 3:
            break
     print("String ended at State : ",state)
     if (state==3):
          print("Input String is accepted by DFA")
     else:
          print("Input String is rejected by DFA")
               
DFA()

