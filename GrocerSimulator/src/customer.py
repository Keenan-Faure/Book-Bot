import address as Address

class Customer:
    def __init__(self, first_name:str, last_name:str, address:Address, payment_method):
        self.__first_name = str(first_name)
        self.__last_name = str(last_name)
        self.__address = address
        self.__payment_method = payment_method
    
    #gettors and settors
    def get_first_name(self):
        return self.__first_name
    def get_last_name(self):
        return self.__last_name
    def get_address(self):
        return self.__address
    def get_payment_method(self):
        return self.__payment_method
    
    def set_first_name(self, newFirstName:str):
        self.__first_name = newFirstName
    def set_last_name(self, newLastName:str):
        self.__last_name = newLastName
    def set_address(self, newAddress:Address):
        self.__address = newAddress
    def set_payment(self, newPaymentMethod):
        self.__payment_method = newPaymentMethod