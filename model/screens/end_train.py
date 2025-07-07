from model.screens.base_screen import Screen
import time
class EndTrain(Screen):
    def __init__(self,options):
        super().__init__(options)
        self.finishButton:str = options.imagePath + "control/finishButton.jpg"
        self.cancelButton:str = options.imagePath + "control/cancelButton.jpg"
    def run(self):
        print("This is the End Training Menu")
        time.sleep(self.WAITTIME)

        buttonX, buttonY = self.findImage(self.finishButton)
        self.clickOnImage(buttonX,buttonY)

        time.sleep(3)

        self.clickOnImage(buttonX, buttonY)

        time.sleep(5)

        self.clickOnImage(buttonX, buttonY)
        self.clickOnImage(buttonX, buttonY)

        buttonX, buttonY = self.findImage(self.cancelButton)
        self.clickOnImage(buttonX, buttonY)
        time.sleep(8)