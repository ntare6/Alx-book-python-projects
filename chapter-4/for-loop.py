#repeats its body loop element

word=input("please enter your name ")


for name in word:
    print(name)
    
    
for i in range(10):
    print(i)    


for i in (0,1,2,3,4,5,7,8,9,10):
    print(i)
    
 #starts,end,next   
for i in range(0,50,5):
    print(i)
    
for i in range(10,0,-1):
    print(i)
    
    
uni="auca"

if "u" in uni:
    print("yes u is in uni")
else:
    print("no try another letter")
            
position=uni[2]
print(position)

import random
choice="index"
high=len(choice)
low=-len(choice)
for i in range(10):
    position=random.randrange(low,high)
    print("word[",position, "]\t",choice[position])
    
    
message=input("enter your message ")

new_message=""
#constant never change it
VOWELS="aeiou"

for letter in message:
    if letter.lower() not in VOWELS:
        new_message +=letter
        print("your new_message is",new_message)
        
food="pizza"
pos=food[:]
print(pos)            



