list = ["telent","computer","institute"]
print(list)
cont = 0
count = 0 
for name in list : 
    for j in name : 
        if j == 'a' or j == 'e' or j == 'i' or j == 'o' or j == 'u' : 
            cont+=1
        count+=1
print("Vowel : ",cont)
print(count)




    



