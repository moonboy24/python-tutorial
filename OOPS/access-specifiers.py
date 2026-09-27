
class Parent:
    def __init__(self):
        self.public_var = "I am Public"
        self._protected_var = "I'm Protected"
        self .__private_var = "I'm Private"

    def access_from_same_class(self):
        print("Inside Parent class:")
        print("Public:", self.public_var)
        print("Protected:", self ._protected_var)
        print("Private:", self .__private_var)

class Child(Parent):
    def access_from_subclass(self):
        print("Inside Child class (Subclass):")
        print("Public:", self.public_var)
        print("Protected:", self._protected_var)
        try:
            print("Private:" ,self.__private_var)       
            # If we use _Parent__protected_var , we can access the parent method even if it is private method 
            # Same applies for accessing from any class
        except AttributeError:
            print("Private cannot be accessed (AttributeError)")
            
class Stranger:
    def access_from_other_class(self, obj):         # Here Obj is the reference to the parent so we can access it from stranger class like inheritance
        print("Inside Stranger Class")
        print("Public Class", obj.public_var)
        print("Protected Class" , obj._protected_var)  # Not Recommended
        try:
            print("Privated class" , obj.__private_var)
        except AttributeError:
            print("Can't access Private Class")
        
        
p = Parent()
c = Child()
s= Stranger()

print("\nAccess from SAME class:")
p.access_from_same_class()

print("\nAccess from SUBCLASS:")
c.access_from_subclass()


print("\nAccess from OTHER CLASS:")
s.access_from_other_class(p)