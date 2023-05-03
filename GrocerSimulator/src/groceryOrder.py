import customer as Customer
import groceryList as GroceryList

class GroceryOrder:

    def __init__(self, customer, groceryList):
        self.__customer = customer
        self.__groceryList = groceryList

    def print_receipt(self):
        print("printing order on a receipt")
    
    def orderConfirm(self, warehouse):
        print("does calculations on the order")
    
    #gettors and settors
    def get_customer(self):
        return self.__customer
    def get_grocery_list(self):
        return self.__groceryList
    def set_customer(self, newCustomer: Customer):
        self.__customer = newCustomer
    def set_grocery_list(self, newGroceryList: GroceryList):
        self.get_grocery_list = newGroceryList