# SIMPLE ORDERING  TIP CALCULATOR
"""
    Input the orders
    Calculate the total
    Calculate tip if given
"""
class Order:
    
    def __init__(self):
       self.storeName = "ALRA"
       self.foodPrices =  {
            "Adobo": 150.00,
            "Sinigang": 180.50,
            "Lechon Kawali": 220.75,
            "Pancit Bihon": 120.00,
            "Lumpia Shanghai (6pcs)": 80.00,
            "Chicken Inasal": 165.25,
            "Sisig": 190.00,
            "Halo-Halo": 95.50,
            "Turon (2pcs)": 40.00,
            "Garlic Rice (single)": 35.00
        }
       
    def __str__(self):
        return f"Welcome to {self.storeName}!"
    
    def askTip():
        """display the input field to ask the amount of the tip

        Returns:
            tip (float): amount of the tip
        """
        
        return float(input("Tip Amount: "))
        


    def displayOrder(self, products):
        bill = 0
        
        """process the order for checkout

        Args:
            products (list): _description_
            
        Return:
            bill (float): _description_
        """
        
        for productKeys in products:
            bill += self.foodPrices[productKeys]        
        return print(bill)
    
    def checkout(self, products, tip):
        bill = 0
        
        """process the order for checkout

        Args:
            products (list): _description_
            
        Return:
            bill (float): _description_
        """
        
        for productKeys in products:
            bill += self.foodPrices[productKeys]
        
        return print(bill + float(tip))
    
    
  