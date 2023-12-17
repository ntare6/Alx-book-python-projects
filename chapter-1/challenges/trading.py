#user picks a game
#if 


import random


my_number=int(input("i'm your owner and the number i'ma pick is "))
computer_guess=random.randrange(10) +1

tries=1

while computer_guess != my_number:
    print("i'm your computer and the number you just picked is",computer_guess)
    my_number=int(input("i'm your owner and i'm entering another number and this time i pick "))
    
    
   
    tries +=1
    
    if tries==5:
        print("running out of options")
        break
    
    
print("my number wa ",my_number)    
    
        
        