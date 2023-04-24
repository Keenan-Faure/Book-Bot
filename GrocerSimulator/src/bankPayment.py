import bank as Bank

class BankPayment():
    def __init__(self, balance: float, bank: Bank):
        self.__balance = float(balance)
        self.__bank = bank

    def withdraw(self, amount: float):
        if(self.__balance < amount):
            raise Exception("Not enough Money in Account")
        else:
            self.__balance -= float(amount)
            self.__balance = round(self.__balance, 2)
    def deposit(self, amount: float):
        if(amount >= 0):
            self.__balance += float(amount)
            self.__balance = round(self.__balance, 2)
        else:
            raise Exception("Cannot deposit: " + str(amount))

    #gettors and settors
    def get_balance(self):
        return float(self.__balance)
    def get_bank(self):
        return self.__bank
    
    def set_balance(self, newBalance: float):
        if(newBalance >= 0):
            self.__balance = newBalance
        else:
            raise Exception("Attempting to set invalid amount")
    def set_bank(self, newBank: Bank):
        self.__bank = newBank
