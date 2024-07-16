import random

user = input("Enter Choice (Ston,Papaer,Scissors)")
outcomes = ["stone","paper","scissors"]
computer = random.choice(outcomes)

if user == computer :
    print("enter players selected same 'it's tie!'")

elif user == "stone" : 
    if computer == "scissors" : 
        print("Stone smasser Scissors! you Win!")
    else :
        print("PAper cover stone! you lose.")

elif user == "paper" : 
    if computer == "rock" : 
        print("paper covers rock! you win")
    else : 
        print("Scissors cuts paper ! you lose!")

elif user == "scissors" : 
    if computer == "paper": 
        print("Scissors cuts paper! you win!")
    else :
        print("stone smashes scissors! you lose!")
