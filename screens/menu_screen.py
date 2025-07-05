import time
from screens.base_screen import Screen

class MenuScreen(Screen):
    def __init__(self, imagePath):
        super().__init__(imagePath)
        self.trainImg = imagePath+"control/train.jpg"

    def run(self):
        print("This is the Menu Screen")
        time.sleep(self.WAITTIME)
        buttonX, buttonY = self.findImage(self.trainImg)
        self.clickOnImage(buttonX, buttonY)
        
        # Import here to avoid circular import
        from screens.training_menu_screen import TrainingMenuScreen
        TrainingMenuScreen(self.imagePath).run()