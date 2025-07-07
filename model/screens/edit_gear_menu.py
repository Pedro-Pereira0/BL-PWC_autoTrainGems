import time
from model.screens.base_screen import Screen

class EditGearMenu(Screen):
    def __init__(self,options):
        super().__init__(options)
        self.nextImage:str = options.imagePath + "control/nextButton.jpg"

    def run(self):
        print("This is the Edit Gear Menu")
        time.sleep(self.WAITTIME)

        buttonX, buttonY = self.findImage(self.nextImage)
        self.clickOnImage(buttonX,buttonY)
        
        # Import here to avoid circular import
        from model.screens.final_confirmation_menu import FinalConfirmationMenu
        FinalConfirmationMenu(self.options).run()