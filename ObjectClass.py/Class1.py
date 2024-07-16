# class talent:
    # x = 5
# a = talent
# print(a.x)

class item:
    def __init__(self,name,surname):
        self.nm = name 
        self.srnm = surname 
    def show(self):
        print("your name is "+ self.nm)
        print("your surname name is "+ self.srnm)
        print("your full name is " + self.nm + "" + self.srnm)
a = item('talent','computer')
a.show()
