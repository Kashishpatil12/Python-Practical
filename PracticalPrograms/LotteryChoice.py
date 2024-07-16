print("------------------------------------------------")
import random

user = input("Enter one number in 10 to 100 : ")
list1 = [10,20,30,40,50,60,70,80,90]
computer = random.choice(list1)

if user == computer :
    print("You Win!")
else : 
    print("You Lose!")