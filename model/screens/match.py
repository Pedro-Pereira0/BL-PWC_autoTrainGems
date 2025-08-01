import time
from model.screens.base_screen import Screen

class Match(Screen):
    def __init__(self, options):
        super().__init__(options)
        self.startMatch:str = options.imagePath + "control/startMatchButton.jpg"
        self.okButton:str = options.imagePath + "control/okButton.jpg"
        self.nextButton:str = options.imagePath + "control/nextButton.jpg"

    def run(self, isRevenueMatch = False):
        time.sleep(5)
        buttonX, buttonY = self.findImage(self.startMatch)
        if(buttonX != None and buttonY != None): 
            self.clickOnImage(buttonX, buttonY)
            time.sleep(20)

            buttonX, buttonY = self.findImage(self.okButton)
            self.clickOnImage(buttonX, buttonY)

            # #There is only a next button if its a Revenue match
            # if(isRevenueMatch == True):
            #     buttonX, buttonY = self.findImage(self.nextButton)
            #     self.clickOnImage(buttonX, buttonY)

            time.sleep(5)
