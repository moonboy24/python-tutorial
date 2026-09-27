
# Lambda

# add = lambda a,b : a+b
# square = lambda c : c**2
# print(add(4,5))
# print(f"Square is {square(5)}")

# Map

# fruits = ["apple" , "mango" , "cherry"]
# result = list(map(lambda fruit : fruit.upper() , fruits))
# print(result)


# Filter

# nums = [1,2,3,4,5,6]
# even = list(filter(lambda x : x%2 == 0 , nums))
# print(even)



# Reduce
from functools import reduce

nums = [1,2,3,4]
total = reduce(lambda a,b : a+b , nums)
print(total)


num = [50 , 100 , 45 ]
maxi = reduce(lambda a,b : a if a> b else b , num)
print(maxi)