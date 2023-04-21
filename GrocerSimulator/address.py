class Address:
    def __init__(
            self,
            address1: str,
            address2: str,
            postalcode: int,
            city: str,
            country: str
        ):
        self.__address1 = address1
        self.__address2 = address2
        self.__postalcode = postalcode
        self.__city = city
        self.__country = country
    
    #gettors and settors
    def get_address1(self):
        return self.__address1
    def get_address2(self):
        return self.__address2
    def get_postalcode(self):
        return self.__postalcode
    def get_city(self):
        return self.__city
    def get_country(self):
        return self.__country
    
    def set_address1(self, newAddress1):
        self.__address1 = newAddress1
    def set_address2(self, newAddress2):
        self.__address2 = newAddress2
    def set_postalcode(self, newPostalCode):
        self.__postalcode = newPostalCode
    def set_city(self, newCity):
        self.__city = newCity
    def set_country(self, newCountry):
        self.__country = newCountry