menu = []
con =1

no=int(input("Enter number : "))
for i in range (1,no+1) : 
    name = str(input("Enter a name : "))
    menu.append(name)
print(menu)
    #for i in menu 
    # print(i)
while con==1:
    choice = int(input("[1] add to item\n 2 for delete the your list \n 3 for remove the item \n 4 Remove item indexwise\n 5 for Clear\n"))
    print(menu)
    
    if choice==1 : 
        no2 =int(input("Enter number you want to add in the list : "))

        for i in range(1,no2+1):
            item=str(input("Enter name you want to add the list :"))
            menu.append(item)
        print(menu)
        for i in menu :
            print(i)
        
    if choice ==2 : 
        del menu 
        print("Delete your list ")
    print(menu)

    if choice==3 :
        print("Remove the name")
        item2 = str(input("Enter a name you want remove the list : "))
        menu.remove(item2)
        print(menu) 
    if choice == 4 :
        print("pop the item indexwise ")
        index = int(input("Enter the index number"))
        menu.pop(index)
        print(menu)
    if choice == 5 : 
        print("clear the data")
        menu.clear()
        print(menu)
    con=int(input("DO you want to continue the upadate in loop 1 for yes others for exit..."))