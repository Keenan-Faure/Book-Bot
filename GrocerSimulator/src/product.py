class Product:
    def __init__(self, code: str="", title: str="", qty: int=0, price:float=0.0, vendor: str=""):
        self.code  = str(code)
        self.title = str(title)

        if(qty == "" or qty == None): 
            self.qty   = 0
        else: self.qty = int(qty)

        if(price == "" or price == None):
            self.price   = 0.0
        else: self.price = float(price)

        self.vendor = str(vendor)
    
    #gettors and settors
    def get_code(self):
        return self.code
    def get_title(self):
        return self.title
    def get_qty(self):
        return self.qty
    def get_price(self):
        return self.price
    def get_vendor(self):
        return self.vendor
    
    def set_code(self, newCode):
        self.code = newCode
    def set_title(self, newTitle):
        self.title = newTitle
    def set_qty(self, newQty):
        self.qty = newQty
    def set_price(self, newPrice):
        self.price = newPrice
    def set_vendor(self, newVendor):
        self.vendor = newVendor