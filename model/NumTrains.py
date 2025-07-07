from util.Exceptions import InvalidNumber

class NumTrains():
    def __init__(self, nTrainString):
        try:
            self.numTrains:int = int(nTrainString)

            if self.validate() == False:
                raise InvalidNumber("Invalid number. Must be a number, higher or equal to 0.")
            
        except Exception as err:
            raise InvalidNumber("Invalid number. Must be a number, higher or equal to 0.", err)
        
    def validate(self) -> bool:
        if(self.numTrains < 1):
            return False
        else:
            return True