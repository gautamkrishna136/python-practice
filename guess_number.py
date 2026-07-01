import random 
target=random.randint(1,100)
while True:
    userchoice=input("guess the target or quit")
    if (user_choice =="quit"):
        break
    userchoice=int(userchoice)
    if(userchoice==target):
        print("success:correct guess")
        break
    elif(userchoice<target):
        print("your guess is to low ...take bigger guess")
    else:
        print("your guess is to high...take smaller guess")
print("--------game over---------")
       