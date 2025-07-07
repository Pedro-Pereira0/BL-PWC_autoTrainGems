import time
from model.screens.base_screen import Screen

class TrainingMenuScreen(Screen):
    def __init__(self, options):
        super().__init__(options)
        self.typeTrain:str = options.imagePath + "control/typeTrain.jpg"
        self.prevTrain:str = options.imagePath + "control/leftSideButton.jpg"
        self.nextImg:str = options.imagePath + "control/nextButton.jpg"

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
        from model.screens.select_player_screen import SelectPlayerScreen
        SelectPlayerScreen(self.options).run()