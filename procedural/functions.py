# Example 1
def add(*args):
    total = 0

    for num in args:
        total += num
        # 0 += 1
        # 1 += 3
        # 4 += 5
        # 9 += 10
        # Total = 19
        
    return total

print(add(1,3,5,10))

# Example 2

def create_profile(**kwargs):
    print("User Profile")
    for key , value in kwargs.items():
        print(f"{key} : {value}")

print(create_profile(name = 'Star' , age = 20 , job = 'HR manager'))
print(create_profile(name = 'Moon' , age = 20 , job = 'Manager'))