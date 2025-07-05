import time
from screens.base_screen import Screen

class SelectPlayerScreen(Screen):
    def __init__(self, imagePath):
        super().__init__(imagePath)
        self.playerImg = imagePath + "player/kuni.jpg"
        self.nextImg = imagePath + "control/nextButton.jpg"

    def run(self):
        print("This is the Select player screen!")
        time.sleep(self.WAITTIME)

        buttonX, buttonY = self.findImage(self.playerImg)
        self.clickOnImage(buttonX, buttonY)
        
        #If the buttons are None scroll down until the player is found
        buttonX, buttonY = self.findImage(self.nextImg)
        self.clickOnImage(buttonX,buttonY)

        # Import here to avoid circular import
        from screens.edit_support_screen import EditSupportScreen
        EditSupportScreen(self.imagePath).run()