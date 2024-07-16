class Talent :
    def __init__(self,name,surname):
        self.fname = name  
        self.lname = surname 

    def hello(self) : 
        print("hello",self.fname)

    def sum(self,a,b) :
        return a+b
        
p1 = Talent("Kashish","Patil")
print(p1.fname)
print(p1.lname)

print("hello 123")
p1.hello()

print(p1.sum(3,5))


