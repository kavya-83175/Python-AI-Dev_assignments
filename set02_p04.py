# 2.4 The Shopping Cart Bug

def add_to_cart(item, cart=[]): #Default arguments are only evaluated once, only during initialization
    if(len(cart)==0):
        cart=[]
    cart.append(item)
    return cart

print(add_to_cart("pen"))
print(add_to_cart("book"))
print(add_to_cart("bag"))