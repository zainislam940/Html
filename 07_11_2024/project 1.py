import random
def gameWin(comp,you):
    if comp== you:
        return none
    elif comp=='s':
        if you=='w':
            return false
        elif you=='g':
            return True
    elif comp=='w':
     if you=='g':
            return false
     elif you=='s':
            return True
     elif comp=='g':
         if you=='s':
            return false
     elif you=='w':
            return True
    comp = input("computer turn:Snake(s) Water(w) Gun(g)?")
randno = random.randint(1,3)

if randno == 1: 
    comp = 's'
elif randno == 2: 
    comp = 'w'
elif randno == 3: 
    comp = 'g'
    you = input("your turn:Snake(s) Water(w) Gun(g)?")
a = gameWin( comp,you)
print(f"comp chose{comp}")
print(f"your chose{you}")

if a==None:
   print("the game is tie!")
elif a:
   print("you win!")
else:
      print("you lose!")