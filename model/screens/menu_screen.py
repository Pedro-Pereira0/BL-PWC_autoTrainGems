import time
from model.screens.base_screen import Screen

class MenuScreen(Screen):
    def __init__(self, options):
        super().__init__(options)
        self.trainImg:str = options.imagePath+"control/train.jpg"

    def run(self):
        print("This is the Menu Screen")
        time.sleep(self.WAITTIME)
        buttonX, buttonY = self.findImage(self.trainImg)
        self.clickOnImage(buttonX, buttonY)
        
        # Import here to avoid circular import
        from model.screens.training_menu_screen import TrainingMenuScreen
        TrainingMenuScreen(self.options).run()