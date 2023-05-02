class Product:
    def __init__(self, code: str="", title: str="", qty: int=0, price:float=0.0, vendor: str=""):
        self.__code  = str(code)
        self.__title = str(title)

        if(qty == "" or qty == None): 
            self.__qty   = 0
        else: self.__qty = int(qty)

        if(price == "" or price == None):
            self.__price   = 0.0
        else: self.__price = float(price)

        self.__vendor = str(vendor)
    
    #gettors and settors
    def get_code(self):
        return self.__code
    def get_title(self):
        return self.__title
    def get_qty(self):
        return self.__qty
    def get_price(self):
        return self.__price
    def get_vendor(self):
        return self.__vendor
    
    def set_code(self, newCode):
        self.__code = newCode
    def set_title(self, newTitle):
        self.__title = newTitle
    def set_qty(self, newQty):
        self.__qty = newQty
    def set_price(self, newPrice):
        self.__price = newPrice
    def set_vendor(self, newVendor):
        self.__vendor = newVendor