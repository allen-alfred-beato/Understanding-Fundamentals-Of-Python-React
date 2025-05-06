from ordering_processes import Order
from utils import Utilities

order = Order()

print(order)

i = 0
for keys, values in order.foodPrices.items():
    i += 1
    print(f"""[{i}]|{keys}: --- ${values}""")
    


products = []
isDone = True
productKeys = list(order.foodPrices.keys())

print("|---Enter Zero[0] to Complete---|")

while(isDone):    
    itemOrder = int(input("Select a Product Number: "))
    
    if itemOrder != 0:
        products.append(productKeys[itemOrder - 1])
    
    if itemOrder == 0:
        isDone = False
     
     
#ask if do tip?
doTip = input("Do you want to add a tip? y/n ").lower()
# amountTip = 

tip = Utilities.delayFunction(Order.askTip, 2) if doTip == "y" else 0
print(tip)
print(products)
order.checkout(products, tip)
