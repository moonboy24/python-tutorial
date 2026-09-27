items = []

while True:
    item = input("Add items(Type 'done' when finished adding)")

    if item.lower() == 'done':
        break
    items.append(item)

print(f"Cart Items are {items}")


def greet():
    print("Welcome")

greet()