cont =0 

while cont < 3  : 
    number = int(input("Enter Lottery number : "))

    if number == 500 or number == 1000 :
        print("Congarts You win jackpot !!!")
        break
    else: 
        print("You lose this jackpot----------------")
    cont+=1  