import random

ch = int(input("--------Plase choose a one number--------\n [1] for STONE \n [2] for PAPER \n [3] for SCISSOR"))

num = random.randrange(0,3)
num2 = random.randrange(0,3)

if ch == num : 
    if ch == num2 : 
     print("You win")
else : 
   print("over")
