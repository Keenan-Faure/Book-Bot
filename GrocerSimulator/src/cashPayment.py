
class CashPayment():
    def __init__(self, cash: float=0.0, cash_owner: str=""):
        self.__cash = float(cash)
        self.__cash_owner = str(cash_owner)
    
    def withdraw(self, amount: float):
        if(self.__cash < amount):
            raise Exception("Not enough Money on hand")
        else:
            self.__cash -= amount
            self.__cash = round(self.__cash, 2)
    def deposit(self, amount: float):
        if(amount >= 0):
            self.__cash += amount
            self.__cash = round(self.__cash, 2)
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