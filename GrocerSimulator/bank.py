import utils as Util

class Bank:
    def __init__(self, name: str, branch_id: int, telephone_number: str):
        self.__name             = name
        self.__branch_id        = branch_id
        self.__telephone_number = self.validate_phone_number(telephone_number)
    
    def validate_phone_number(self, phone_number: str):
        number_count = 0
        phone_number_list = phone_number.split()
        for item in phone_number_list:
            for char in item:
                if(Util.toInt(char) == False):
                    raise Exception("Invalid telephone number")
                else:
                    number_count += 1
        if(number_count != 10):
            phone_number = ""
            raise Exception("Invalid telephone number")
        return phone_number
    
    #gettors and settors
    def get_name(self):
        return self.__name
    def get_branch_id(self):
        return self.__branch_id
    def get_telephone(self):
        return self.__telephone_number
    
    def set_name(self, newName):
        self.__name = newName
    def set_branch_id(self, newBranchId):
        self.__branch_id = newBranchId
    def set_telephone(self, newTelephoneNumber):
        self.__telephone_number = newTelephoneNumber