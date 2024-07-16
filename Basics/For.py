# name = str(input("enter name : "))
# rangeval = int(input("enter range : "))
# for i in range(0,rangeval+1) : 
    #  print(i,":",name)

 
cont = 1
total = 0
while cont  == 1:
    amt = int(input('enter product amount'))
    total = total + amt
    cont = int(input("do you want to continue? press 1 for yes or other to exit"))

print("thanks for shopping with us ", total)
