
# Class name 

class Employee:
    company_name = "Open AI"
    
    @classmethod
    def change_name(cls , new_name):
        cls.company_name = new_name
        
    @staticmethod
    def try_changing_name(new_name):
        company_name = new_name
        
Employee.change_name("Claude")
print("After changing name in Static:" ,Employee.company_name)

Employee.try_changing_name("Gemini")
print("After changing name in Static:" , Employee.company_name)









# Static method
# class math:  
#     @staticmethod
#     def add(x , y):
#         return x+y
# print(math.add(5,10))