
class dad:        #parent class
    def house(self):
        print("red")

class son(dad):   #Child class
    def factory(self):
        print("white")
        
    def house(self):   
        #If u want to change the methods of parent class without changing it , use the same method in the child class and call it
        print("Navy blue")
        
s = son()
s.factory()
s.house()