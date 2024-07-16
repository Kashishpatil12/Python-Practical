class tcit :
    x = 5
    def __init__(self,roll,name):
        self.id = roll
        self.name = roll
    def hello(self):
        print("hello")
    def display(self):
        print("the Roll no is ",self.id,"name is ",self.name)
    
first_obj = tcit(5,"talent")
print(first_obj.x*5)
first_obj.hello()
first_obj.display()