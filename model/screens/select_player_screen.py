import time
import pyautogui as pg
from model.screens.base_screen import Screen

class SelectPlayerScreen(Screen):
    def __init__(self, options):
        super().__init__(options)
        self.playerImg:str = options.player.playerImgPath
        self.filterButton:str = options.imagePath + "control/filterButton.jpg"
        self.nextImg:str = options.imagePath + "control/nextButton.jpg"

    def run(self):
        print("This is the Select player screen!")
        time.sleep(self.WAITTIME)

        buttonX, buttonY = self.findImage(self.playerImg)
        self.clickOnImage(buttonX, buttonY)
        #If the buttons are None scroll down until the player is found
        if buttonX==None or buttonY==None:
            #Will use the filter button as reference to find where to drag
            buttonX, buttonY = self.findImage(self.filterButton)
            startX, startY = buttonX, buttonY - 50
            endX, endY = startX, startY - 80

            for i in range(20):
                pg.moveTo(startX, startY, 0)
                pg.dragTo(endX, endY, 0.3, button='left')
                time.sleep(2)
                button2X, button2Y = self.findImage(self.playerImg)
                if button2X != None and button2Y != None:
                    self.clickOnImage(button2X,button2Y)
                    break
            
        buttonX, buttonY = self.findImage(self.nextImg)
        self.clickOnImage(buttonX,buttonY)

        # Import here to avoid circular import
        from model.screens.edit_support_screen import EditSupportScreen
        EditSupportScreen(self.options).run()