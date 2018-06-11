import random
from goto import goto
options=['R','P','S']
humanchoice=input("Choose an option\n"+"R for Rock\n"+"P for Paper\n"+"S for scissors\n"+"Now choose Wisely : ")
humanchoice=humanchoice.lower()
if   humanchoice=='r':
 h=0
elif humanchoice=='p':
 h=1
elif  humanchoice=='s' :
 h=2
else:
 print("wrong input")
 exit(0)
c=options.index(random.choice(options))
if h==0 and c==1:
 print("""
         
         
         
         
         
                    you lose as Paper beats Rock. so the Computer Wins.You got Terminated.
         
         
         
         
         
                    """)
if h==1 and c==0:
 print("""
         
         
         
         
         
                    you win as Paper beats Rock. so the Human Won..They will have their revenge.
         
         
         
         
         
                   """)
if h==1 and c==2:
 print("""
         
         
         
         
         
                    you lose as Scissors beats Paper. so the Computer Won.You got Terminated.
         
         
         
         
         
                    """)
if h==2 and c==1:
 print("""
         
         
         
         
         
                    you win as Scissors beats Paper. so the Human Won..They will have their revenge.
         
         
         
         
         
                    """)
if h==2 and c==0:
 print("""
         
         
         
         
         
                    you lose as Rock beats Scissors. so the Computer Won.You got Terminated.
         
         
         
         
         
                    """)
if h==0 and c==2:
 print("""
         
         
         
         
         
                    you win as Rock beats Scissors. so the Human Won.They will have their revenge.
         
         
         
         
         
                   """)
