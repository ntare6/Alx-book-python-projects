#create a program that asks user for questions
#if he gets it right add one to his marks

score=0

message=input("welcome to quiz game do you wanna play if yes type y or q to quit ")


if message=="y":
    print("okay let's move to the next question ")
    
else:
    quit()
    
    
question=input("whose the fourty forth president of the USA ")
if question=="barack obama":
    score +=1
    print("that's right")
else:
    print("that was not right")
question=input("whose the president of Rwanda ")
if question=="kagame":
    score +=1
    print("that's right")
else:
    print("that was not right")
question=input("who's the president of chile ")
if question=="javier milei":
    score +=1
    print("that's right")
    
else:
    print("that was not right")
    
print("thank you for taking your time we'll let you know your score")
print("thank you for your patience your score is",score, "out of 3","see you soon")    
            
        
    
    
    