from model.Type import Type
class EnergyType():
 imgPath = "img/energy/"
 def __init__(self, num):
    match int(num):
        case Type.SMALL:
            self.energyImgPath = self.imgPath + "small.jpg"
        case Type.MEDIUM:
            self.energyImgPath = self.imgPath + "medium.jpg"
        case Type.BIG:
            self.energyImgPath = self.imgPath + "big.jpg"