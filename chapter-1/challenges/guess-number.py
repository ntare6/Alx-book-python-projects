#computer picks a number and user try to guess it
#initialize try
#if try equals 5 stop the program
#print the chasting message 
#while number is not right
#and if number is greater computer tells user to pick a smaller number
#else 
#computer tells user to pick a higher number
#print the  congs message

import random

number=random.randrange(10) +1
guess=int(input("please guess the number "))

tries=1

while guess != number:
    if guess < number:
        print("pick a higher number")
        
    else:
        print("pick a smaller number")
        
    guess=int(input("please guess the number"))
    
    tries +=1
    
    if tries==5:
        print("running out of options")
        break
    
    
print("your number was",number)    
    
        
        