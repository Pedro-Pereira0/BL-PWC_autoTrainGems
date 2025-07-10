from model.Type import Type
from util.Exceptions import InvalidEnergyException

class EnergyType():
 imgPath = "img/energy/"
 def __init__(self, num):
    match num:
        case Type.SMALL.value:
            self.energyImgPath = self.imgPath + "small.jpg"
        case Type.MEDIUM.value:
            self.energyImgPath = self.imgPath + "medium.jpg"
        case Type.BIG.value:
            self.energyImgPath = self.imgPath + "big.jpg"
        case _:
            raise InvalidEnergyException("Invalid energy")