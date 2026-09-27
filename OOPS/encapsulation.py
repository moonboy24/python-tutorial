
class Order:
    def __init__(self , customer_name , items, total_amount, discount):
        self.customer_name = customer_name
        self.items = items
        self.__total_amount = total_amount
        self.__discount = discount
    
    def __calculate_final(self): # private helper method
        return self.__total_amount - self.__discount

    def _get_admin_view(self): # protected method
        return {
            "Customer": self.customer_name,
            "Items": self.items,
            "Total Amount": f"₹{self.__total_amount}",
            "Discount Applied": f"{self.__discount}",
            "Final Bill": f"₹{self.__calculate_final()}"
        }
        
    def get_customer_view(self):
        return{
            "Customer" : self.customer_name,
            "Items" : self.items,
            "Final Bill" : f"₹{self.__calculate_final()}"
        }
        
class Admin_portal:
    def show_order(self, Order):
        return Order._get_admin_view()
    
class customer_portal:
    def show_order(self, Order):
        return Order.get_customer_view()
    
order1 = Order("Harshu" , ["Ellaneer Payasam" , "Gobi Rice"], 250, 50)


admin = Admin_portal()
customer = customer_portal()


print("Admin Portal")
print(admin.show_order(order1))

print("Customer Portal")
print(customer.show_order(order1))