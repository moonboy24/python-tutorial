

class Student:
    
    def __init__(self, name , grade):
        self.name = name
        self.grade = grade
        
    def display(self):
        print(f"{self.name} grade is {self.grade}")
        
s1 = Student("Harshu" , 95)
s2 = Student("Shreya" , 92)
s3 = Student("Luna" , 93)

s1.display()
s2.display()
s3.display()