
def outer(msg):
    def inner():
        return f"Message is {msg}"
    return inner

say_hi = outer("Sounds good")

print(say_hi())