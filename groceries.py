grocerylist = ["Milk", "Cheese", "Sausage"]
shoppingcart = ["Milk", "Cheese", "Sausage"]

 
# zip is vergelijken
# x=grocerylist
# y=shoppingcart
for x, y in zip(grocerylist, shoppingcart):
    if x!=y:
        print("Continue Shopping")
    if x==y:
        print("Done Shopping")
   

    
    
