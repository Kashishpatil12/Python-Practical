# namelist = open("NameFile.txt","w")
# namelist.write("Kashish priya sidhhi kanan prachi neha")

namelist = open("NameFile.txt","r")
name = namelist.readlines()
# cont=0
# for i in l : 
    # l = i.split(" ")
    # for n in l :
        # print(n)
        # cont +=1   
# print(cont)

count = 0 
for a in name : 
    name1 = a.split(" ") 
    for i in name1 : 
        if "a" in i:
            count +=1

print(count)