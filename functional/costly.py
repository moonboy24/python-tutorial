
from functools import reduce

prices = [250 , 1550 , 5000]

expensive = list(filter(lambda x : x > 1000 , prices))
total = reduce(lambda a,b : a+b , expensive)

print(total)