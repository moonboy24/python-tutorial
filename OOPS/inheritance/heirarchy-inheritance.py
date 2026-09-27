

class dad:        #parent class
    def house(self):
        print("both sons have rights")

class son1(dad):   #Child class
    def factory(self):
        print("factory belong to son1")

class son2(dad):
    def market(self):
        print("market belong to son2")
        
s1 = son1()
s1.factory()
s1.house()

s2 = son2()
s2.market()
s2.house()