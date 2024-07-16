
def fac(a) : 
    print("Factorial : " ,end=" ")
    fac = 1

    for i in range(1,a+1) :
        fac = i * fac 
    print(fac)

def prime(x) : 
    print("Prime : " ,end=" ")
    
    flag = 0 
    for i in range(1,x):
        if x%2==0:
            flag=1
            break
    if flag == 0 : 
        print("number is prime")
    else :
        print("number is not prime")
    