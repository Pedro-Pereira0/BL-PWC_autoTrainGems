import time
from screens.base_screen import Screen

class EditGearMenu(Screen):
    def __init__(self,imagePath):
        super().__init__(imagePath)
        self.nextImage = imagePath + "control/nextButton.jpg"

    def run(self):
        print("This is the Edit Gear Menu")
        time.sleep(self.WAITTIME)

        buttonX, buttonY = self.findImage(self.nextImage)
        self.clickOnImage(buttonX,buttonY)
        
        # Import here to avoid circular import
        from screens.final_confirmation_menu import FinalConfirmationMenu
        FinalConfirmationMenu(self.imagePath).run()