from model.screens.base_screen import Screen
import time
class EndTrain(Screen):
    def __init__(self,options):
        super().__init__(options)
        self.finishButton:str = options.imagePath + "control/finishButton.jpg"
        self.missionProgress:str = options.imagePath + "control/TMP.jpg"
        self.cancelButton:str = options.imagePath + "control/cancelButton.jpg"
    def run(self):
        print("This is the End Training Menu")
        time.sleep(self.WAITTIME)

        buttonX, buttonY = self.findImage(self.finishButton)
        self.clickOnImage(buttonX,buttonY)

        while True:
            buttonX1, buttonY2 = self.findImage(self.missionProgress)
            if buttonX1 != None and buttonY2 != None:
                self.clickOnImage(buttonX, buttonY)
                break
            else:
                self.clickOnImage(buttonX, buttonY)

        time.sleep(5)

        self.clickOnImage(buttonX, buttonY)

        time.sleep(5)

        self.clickOnImage(buttonX, buttonY)

        time.sleep(5)

        buttonX, buttonY = self.findImage(self.cancelButton)
        self.clickOnImage(buttonX, buttonY)
        time.sleep(8)