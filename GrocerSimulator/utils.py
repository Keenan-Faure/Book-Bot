class Utils:
    
    @staticmethod
    def isInt(number):
        if(number.isnumeric()):
            return True
        elif(isinstance(number, (int, float))):
            if("True" in number):
                return False
            elif("False" in number):
                return False
            return True
        else:
            return False
