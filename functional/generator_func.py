
def get_num(n):
    for i in range(n):
        yield i
        
for num in get_num(5):
    print(num)