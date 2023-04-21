import payment as Payment
import bank as Bank

class BankPayment(Payment):
    def __init__(self, balance: float, bank: Bank):
        self.__balance = balance
        self.__bank = bank

    #gettors and settors
    def get_balance(self):
        return self.__balance
    def get_bank(self):
        return self.__bank
    
    def set_balance(self, newBalance: float):
        if(newBalance >= 0):
            self.__balance = newBalance
        else:
            raise Exception("Attempting to set invalid amount")
    def set_bank(self, newBank: Bank):
        self.__bank = newBank
