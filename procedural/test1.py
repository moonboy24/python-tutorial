delivery_partner = "Swiggy"

def hotel():
    item = "pizza"

    def order_now():
        quantity = 2
        print(f"Odering {quantity} {item} using {delivery_partner}")
    order_now()

hotel()