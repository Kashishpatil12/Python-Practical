class xyz :
    def __init__(self,name,salary) :
        self.a = name 
        self.b = salary
    def printdata(self) :
        print(self.a," ",self.b)
    
class abc(xyz):
    def __init__(self, name, salary,group):
        super().__init__(name, salary)
        self.g = group
    def get_group_name(self):
        print(self.g)

x = abc("Khushi","50000",1200)
x.printdata()
x.get_group_name()
