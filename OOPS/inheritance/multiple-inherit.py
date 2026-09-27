

class dad:        #parent class
    def house(self):
        print("dad has shop")
        
class mom:
    def shop(self):
        print("mom has shop")

class daughter(dad,mom):   #Child class
    def factory(self):
        print("factory belong to daughter")

d = daughter()
d.shop()
d.factory()
d.house()