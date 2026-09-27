

def add(x):
    return x+2

def multily(x):
    return x*2

def compose(x):         #f(g(x))
    return add(multily(x))

print(compose(2))