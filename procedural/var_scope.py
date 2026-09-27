# L -> E -> G -> B

#Local variable

def order():
    food = "Fried Rice"
    print("Your order is" , food)
order()

#Enclosing

def card():
    discount = 10

    def checkout():
        print("Apllying discount of: $",discount)
    checkout()
card()

#Global 

user_id = "moonboy"

def homepage():
    print("Welcome", user_id)

def profile():
    print("Welcome to profile page", user_id)

homepage()
profile()

#Built-in

print(__file__) #Shows the path of the file or folder you are in 