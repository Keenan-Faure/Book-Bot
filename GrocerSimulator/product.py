class Product:
    def __init__(self, code, title, qty, price):
        self.__code = code
        self.__title = title
        self.__qty = qty
        self.__price = price
    
    #gettors and settors
    def get_code(self):
        return self.__code
    def get_title(self):
        return self.__title
    def get_qty(self):
        return self.__qty
    def get_price(self):
        return self.__price
    
    def set_code(self, newCode):
        self.__code = newCode
    def set_title(self, newTitle):
        self.__title = newTitle
    def set_qty(self, newQty):
        self.__qty = newQty
    def set_price(self, newPrice):
        self.__price = newPrice