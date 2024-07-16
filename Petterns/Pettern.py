star = int(input("Enter stars number : "))
a = 65
for i in range(0,star) : 
    for j in range(0,star) :
        print(chr(a),end=" ")
        a+=1
    print()

