class Employee : 
    Empcount = 0 
    
    def __init__(self,name,salary):
         self.name = name 
         self.salary = salary 
         Employee.Empcount +=1
    
    def displayCount(self) :
         print("Total Employee %d "% Employee.Empcount)

    def displayEmployee(self) : 
         print("Name : ",self.name,", Salary : ",self.salary)
    

emp1 = Employee("Mahadev",21500)
emp2 = Employee("Shiv",25000)
emp3 = Employee("Bhole",50000)

emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()

print("Total Employee %d"% Employee.Empcount)