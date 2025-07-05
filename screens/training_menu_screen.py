import time
from screens.base_screen import Screen

class TrainingMenuScreen(Screen):
    def __init__(self, imagePath):
        super().__init__(imagePath)
        self.typeTrain = imagePath + "control/typeTrain.jpg"
        self.prevTrain = imagePath + "control/leftSideButton.jpg"
        self.nextImg = imagePath + "control/nextButton.jpg"

    def run(self):
        print("This is the Training Menu Screen")
        time.sleep(self.WAITTIME)
        while True:
            buttonX, buttonY = self.findImage(self.typeTrain)
            time.sleep(0.5)
            if buttonX == None or buttonY == None:
                button1X, button1Y = self.findImage(self.prevTrain)
                self.clickOnImage(button1X, button1Y)
            else:
                break

        button2X, button2Y = self.findImage(self.nextImg)
        self.clickOnImage(button2X, button2Y)

        # Import here to avoid circular import
        from screens.select_player_screen import SelectPlayerScreen
        SelectPlayerScreen(self.imagePath).run()