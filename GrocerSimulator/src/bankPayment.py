import bank as Bank

class BankPayment():
    def __init__(self, amount: float, bank: Bank):
        self.__amount = float(amount)
        self.__bank = bank

    def withdraw(self, amount: float):
        if(self.__amount < amount):
            raise Exception("Not enough Money in Account")
        else:
            self.__amount -= float(amount)
            self.__amount = round(self.__amount, 2)
    def deposit(self, amount: float):
        if(amount >= 0):
            self.__amount += float(amount)
            self.__amount = round(self.__amount, 2)
        else:
            raise Exception("Cannot deposit: " + str(amount))

    #gettors and settors
    def get_amount(self):
        return float(self.__amount)
    def get_bank(self):
        return self.__bank
    
    def set_amount(self, newBalance: float):
        if(newBalance >= 0):
            self.__amount = newBalance
        else:
            raise Exception("Attempting to set invalid amount")
    def set_bank(self, newBank: Bank):
        self.__bank = newBank
