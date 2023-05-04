import product as Product

class GroceryList:
    def __init__(self, product_list: list=[]):
        self.__product_list = product_list
    
    def reset_list(self):
        self.__product_list = []
        
    def add_product(self, new_product:Product):
        self.__product_list.append(new_product)

    #gettors and settors
    def get_grocery_list(self):
        return self.__product_list
    
    def set_grocery_list(self, newList: list):
        self.__product_list = newList 