import payment as Payment

class CashPayment(Payment):
    def __init__(self, cash: float, cash_owner: str):
        self.__cash = cash
        self.__cash_owner = cash_owner
    
    def withdraw(self, amount: float):
        if(self.__cash < amount):
            raise Exception("Not enough Money on hand")
        else:
            self.__cash -= amount
    def deposit(self, amount: float):
        if(amount >= 0):
            self.__cash += amount
        else:
            raise Exception("Cannot deposit: " + str(amount))
        
    #gettors and settors
    def get_cash(self):
        return self.__cash
    def get_cash_owner(self):
        return self.__cash_owner
    def set_cash(self, amount: float):
        if(amount >= 0):
            self.__cash = amount
        else:
            raise Exception("Attempting to set invalid amount")
    def set_cash_owner(self, newOwner):
        self.__cash_owner = newOwner