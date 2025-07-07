import os
from util.Expections import NonExistingPlayer

class Player():
    imgPath = "img/player/"
    def __init__(self, name):
        self.name = name
        self.playerImgPath = self.imgPath + name + ".jpg"
        if self.validate() == False:
            raise NonExistingPlayer("Player",name,"doesn't exist. Choose a player!")
            

    def validate(self) -> bool:
        if os.path.exists(self.playerImgPath):    
            return True
        else: 
            return False
    