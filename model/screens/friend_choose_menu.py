import time
from model.screens.base_screen import Screen
from model.PlayerGrid import PlayerGrid
import pyautogui as pg

class FriendChooseMenu(Screen):
    def __init__(self,options):
        super().__init__(options)
        self.template:str = options.imagePath + "control/playerTemplate.jpg"
        self.notAvailable:str = options.imagePath + "control/notAvailable.jpg"
        self.confirm:str = options.imagePath + "control/confirmButton.jpg"
        self.grid = PlayerGrid(options.centerX, options.centerY)

    
    def run(self):
        print("This is the Friend Choose Menu")
        time.sleep(self.WAITTIME)
        getTheColorPos = 50
        #Get the coordinates for the confirm button
        buttonX, buttonY = self.findImage(self.confirm)

        print(pg.pixel(int(buttonX + getTheColorPos), int(buttonY)))

        pg.moveTo(self.options.centerX, self.options.centerY)
        #Do something to not choose a partner that has been selected
        for i in range(3):
            for y in range(5):
                pg.moveTo(self.grid.collumn[y], self.grid.row[i])
                self.clickOnImage(self.grid.collumn[y], self.grid.row[i])
                if(pg.pixelMatchesColor(int(buttonX+getTheColorPos), int(buttonY), (127, 73, 16))):
                    continue
                else:
                    self.clickOnImage(buttonX,buttonY)