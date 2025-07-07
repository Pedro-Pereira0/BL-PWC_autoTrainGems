import time
from model.screens.base_screen import Screen

class EditSupportScreen(Screen):
    def __init__(self,options):
        super().__init__(options)
        self.addSupportButton = options.imagePath + "control/addSupportButton.jpg"
        self.nextButton = options.imagePath + "control/nextButton.jpg"

    def run(self):
        print("This is the Edit Support Screen!")
        time.sleep(self.WAITTIME)

        buttonX, buttonY = self.findImage(self.addSupportButton)
        self.clickOnImage(buttonX, buttonY)

        # Import here to avoid circular import
        from model.screens.friend_choose_menu import FriendChooseMenu
        FriendChooseMenu(self.options).run()
        print("Back")
        time.sleep(2)

        buttonX, buttonY = self.findImage(self.nextButton)
        self.clickOnImage(buttonX,buttonY)

        # Import here to avoid circular import
        from model.screens.edit_gear_menu import EditGearMenu
        EditGearMenu(self.options).run()