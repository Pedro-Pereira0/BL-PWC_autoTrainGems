import time
from screens.base_screen import Screen

class FriendChooseMenu(Screen):
    def __init__(self,imagePath):
        super().__init__(imagePath)
        self.confirm = imagePath + "control/confirmButton.jpg"

    def run(self):
        print("This is the Friend Choose Menu")
        time.sleep(self.WAITTIME)

        buttonX, buttonY = self.findImage(self.confirm)
        self.clickOnImage(buttonX,buttonY)