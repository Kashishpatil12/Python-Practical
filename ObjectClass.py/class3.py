class employee:
    empcount = 0

    def __init__(self,name,salary) :
        self.name = name
        self.salary = salary
        employee.empcount += 1

    def displayCount(self):
        print("total Employee %d "% employee.empcount)
    def displayemployee(self):
        print("name: ",self.name," salary : ", self.salary)

emp1 = employee("mahadev", 21500)
emp2 = employee("shiv",55000)

emp1.displayemployee()
emp2.displayemployee()
print("Total Employee %d " % employee.empcount)

 