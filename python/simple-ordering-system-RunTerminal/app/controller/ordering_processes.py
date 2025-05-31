# SIMPLE ORDERING  TIP CALCULATOR

class Order:
    """
        Input the orders
        Calculate the total
        Calculate tip if given
    """
    
    def __init__(self):
       self.storeName = "ALRA"
       self.bengProducts = {
            "espresso" : 
                {
                    "americano" : { 'm' : 1, 'x' : 2, 'xl' : 3, 'hot': 4 },
                    "caffe_latte" : { 'm' : 1, 'x' : 2, 'xl' : 3, 'hot': 4 },
                },
            "cold_brew" : {
                    "black" : { 'm' : 1, 'x' : 2, 'xl' : 3},
                    "mocha" : { 'm' : 1, 'x' : 2, 'xl' : 3},
               },
            "milk_based" : {
                    "matcha" : { 'm' : 1, 'x' : 2, 'xl' : 3},
                    "chocolate_match" : { 'm' : 1, 'x' : 2, 'xl' : 3},
               },        
       }
       self.askOrder()
       
       
    def __str__(self):
        return f"Welcome to {self.storeName}!"
    
    def askOrder(self):
        """ 
            Ask the customer for their order.
        """
        orders = []
        orderSelection = list(self.bengProducts.keys())
        state = True
        option = 1
        
        for i in self.bengProducts.keys():
            print(f"[{option}]" + i)
            option += 1        
                
        print(orderSelection)
        
        while(state):
           selectedCategory = int(input("Select Item Number: "))
           if (selectedCategory - 1) == -1:
               state = False
           elif selectedCategory < len(orderSelection) + 1:
               self.listOrder(orderSelection[selectedCategory - 1])
           else:
               print("inavlid input!")
                       
                       
    def listOrder(self, key):
        """Display the selected category

        Args:
            key (_type_): _description_
        """
        state = True
        products = list(self.bengProducts[key].keys())
        while (state):    
            print(products)
    
    def askTip():
        """display the input field to ask the amount of the tip

            Returns:
                tip (float): amount of the tip
        """
        
        return float(input("Tip Amount: "))
        


    def displayOrder(self, products):

        """process the order for checkout

            Args:
                products (list): _description_
                
            Return:
                bill (float): _description_
        """

        bill = 0
                
        for productKeys in products:
            bill += self.foodPrices[productKeys]        
        return print(bill)
    
    def checkout(self, products, tip):

        """process the order for checkout

            Args:
                products (list): _description_
                
            Return:
                bill (float): _description_
        """
        bill = 0
        
        for productKeys in products:
            bill += self.foodPrices[productKeys]
        
        return print(bill + float(tip))
    
    
  