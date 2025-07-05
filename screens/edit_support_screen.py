import time
from screens.base_screen import Screen

class EditSupportScreen(Screen):
    def __init__(self,imagePath):
        super().__init__(imagePath)
        self.addSupportButton = imagePath + "control/addSupportButton.jpg"
        self.nextButton = imagePath + "control/nextButton.jpg"

    def run(self):
        print("This is the Edit Support Screen!")
        time.sleep(self.WAITTIME)

        buttonX, buttonY = self.findImage(self.addSupportButton)
        self.clickOnImage(buttonX, buttonY)

        # Import here to avoid circular import
        from screens.friend_choose_menu import FriendChooseMenu
        FriendChooseMenu(self.imagePath).run()
        print("Back")
        time.sleep(2)

        buttonX, buttonY = self.findImage(self.nextButton)
        self.clickOnImage(buttonX,buttonY)

        # Import here to avoid circular import
        from screens.edit_gear_menu import EditGearMenu
        EditGearMenu(self.imagePath).run()