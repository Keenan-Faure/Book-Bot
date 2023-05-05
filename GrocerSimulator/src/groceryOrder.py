import customer as Customer
import groceryList as GroceryList

from product import *

class GroceryOrder:

    def __init__(self, customer: Customer, groceryList: GroceryList):
        self.__customer = customer
        self.__groceryList = groceryList

        self.orderedProducts = []
        self.totalCost = 0.0

    """
    Confirms the order and prints out a receipt
    returns the products whose quantities should be 
    updated in `Window.Products` and the `totalCost`
    """
    def orderConfirm(self, storeProducts: GroceryList):
        self.remove_zero_qty()
        if(len(storeProducts) <= 0):
            raise Exception("No Products loaded in Store")
        if(len(self.__groceryList.get_grocery_list()) <= 0):
            raise Exception("No Products in Basket")

        for product in self.__groceryList.get_grocery_list():
            if(self.in_stock(product, storeProducts)):
                self.deduct_cost(product, self.__customer)
        return [self.orderedProducts, float(self.totalCost)]
    
    """
    Confirms if there is enough
    Qty to order the item
    raises an Exception (returns None)
    if there is not enough on hand
    or if the code is not found
    """
    def in_stock(self, product: Product, storeProducts:GroceryList):
        for product_on_hand in storeProducts:
            if(product_on_hand.get_code() == product.get_code()):
                if(product_on_hand.get_qty() >= product.get_qty()):
                    self.orderedProducts.append(product)
                    return True
                raise Exception("Not enough quantity for Code '" + product.get_code() + "'")
        raise Exception("No Code found equal to '" + product.get_code() + "'")
        
    """
    Adds the product price to the
    total cost otherwise it 
    raises an Exception if the cost 
    exceeds the current balance
    """
    def deduct_cost(self, product: Product, customer: Customer):
        prod_price = float(product.get_price() * product.get_qty())
        if(prod_price <= float(customer.get_payment_method().get_amount() + self.totalCost)):
            self.totalCost += prod_price
        elif(prod_price > customer.get_payment_method().get_amount()):
            raise Exception("Not enough money to buy x" + str(product.get_qty()) + " of '" +  product.get_code()+ "'")

    """
    Removes zero quantity products from grocery list
    """
    def remove_zero_qty(self):
        new_list = []
        for product in self.__groceryList.get_grocery_list():
            if(product.get_qty() > 0):
               new_list.append(product)
        self.__groceryList.set_grocery_list(new_list)

    #gettors and settors
    def get_customer(self):
        return self.__customer
    def get_grocery_list(self):
        return self.__groceryList
    def set_customer(self, newCustomer: Customer):
        self.__customer = newCustomer
    def set_grocery_list(self, newGroceryList: GroceryList):
        self.get_grocery_list = newGroceryList