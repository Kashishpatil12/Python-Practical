f1 = open("File/File4.txt","w")
for i in range(1,5+1):
    n = input("enter a name \n")
    f1.write(n)

f1 = open("File/File4.txt","r")
print(f1.read())
