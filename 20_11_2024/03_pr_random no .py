import random
randnumber = random.randint(1,100)
print(randnumber)
userguess= None
guesses= 0
while(userguess != randnumber):
 userguess = int(input("enter your guess"))
 if(userguess==randnumber):
   print("you guessed right")
 else:
        if("userguess>randnumber"):
           print("you guessed it wrong! enter a smaller number")
        else:
            print("you guessed it wrong! enter a larger number") 
print(f"you guessed a number in {guesses} guesses")              


