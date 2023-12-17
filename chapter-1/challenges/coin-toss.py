#user toss coin hendred times
#initialize both head and tail and toss
#while toss is less than a hundred keep tossing 
#if draw is head
#increament head
#toss again
#else if draw is tail
#increament tail
#toss again
#print the number of toss and tails
import random
flip=100
tail_count=0
head_count=0

options=["head","tail"]

while flip < 100:
    
    
    
    draw=random.choice(options)
    if draw=="head":
        head_count +=1
    elif draw=="tail":
        tail_count +=1

        
print("your head count is",head_count,"and tail count is",tail_count)            
    
    

