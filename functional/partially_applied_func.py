

from functools import partial

# Step 1 : Define the original function

def calc_price(base_price , tax_rate):
    return base_price * (1+tax_rate)

# Step 2 : Create a partial function with tax rate

price_with_gst = partial(calc_price, tax_rate = 0.18)

print(price_with_gst(1500))
print(price_with_gst(2500))