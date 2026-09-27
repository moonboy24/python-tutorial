#Example 1
amount = 1200
tax = amount*0.18
total = amount + tax

if total > 1000:
    discount = total*0.10
    total -= discount
print(f"Your Total after discounted is {total}")

#Example 2

age = 65
student = 'no'

if age >= 60 or student == 'yes':
    print("Discount is applicable")
else:
    print("No discount")