import time
from model.screens.base_screen import Screen

class FriendChooseMenu(Screen):
    def __init__(self,options):
        super().__init__(options)
        self.confirm = options.imagePath + "control/confirmButton.jpg"

    def run(self):
        print("This is the Friend Choose Menu")
        time.sleep(self.WAITTIME)

        buttonX, buttonY = self.findImage(self.confirm)
        self.clickOnImage(buttonX,buttonY)