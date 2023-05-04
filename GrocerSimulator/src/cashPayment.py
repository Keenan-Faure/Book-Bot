
class CashPayment():
    def __init__(self, cash: float=0.0, cash_owner: str=""):
        self.__amount = float(cash)
        self.__amount_owner = str(cash_owner)
    
    def withdraw(self, amount: float):
        if(self.__amount < amount):
            raise Exception("Not enough Money on hand")
        else:
            self.__amount -= amount
            self.__amount = round(self.__amount, 2)
    def deposit(self, amount: float):
        if(amount >= 0):
            self.__amount += amount
            self.__amount = round(self.__amount, 2)
        else:
            raise Exception("Cannot deposit: " + str(amount))
        
    #gettors and settors
    def get_amount(self):
        return self.__amount
    def get_cash_owner(self):
        return self.__amount_owner
    def set_amount(self, amount: float):
        if(amount >= 0):
            self.__amount = amount
        else:
            raise Exception("Attempting to set invalid amount")
    def set_cash_owner(self, newOwner):
        self.__amount_owner = newOwner