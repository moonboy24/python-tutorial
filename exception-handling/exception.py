
# try , throw , except , finally

try:
    print("Welcome to Zomato!")
    number_of_items = int(input("How many items?: "))
    total_price = 200 * number_of_items
    average_price = total_price / number_of_items
    print("Average price per item: ", average_price)
    
except ZeroDivisionError:
    print("Add atleast 1 item")
    
finally:
    print("always execute")
    