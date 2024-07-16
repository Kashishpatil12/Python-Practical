class vehicle : 
    name = ""
    kind = ""
    color = ""
    value = ""
    def description(self):
        desc_str = "%s is a %s %s worth Rs.%.2f,"% (self.name,self.color,self.kind,self.value)
        return desc_str
    
car1 = vehicle()
car1.name = "maruti"
car1.color ="red"
car1.kind = "CNG"
car1.value = 600000.00

car2 = vehicle()
car2.name = "Toyota"
car2.color = "Black"
car2.kind = "Petrol"
car2.value = 100000.00

print(car1.description())
print(car2.description())