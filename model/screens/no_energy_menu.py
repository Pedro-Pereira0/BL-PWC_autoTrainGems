import time
from model.screens.base_screen import Screen

class NoEnergyMenu(Screen):
    def __init__(self,options):
        super().__init__(options)
        self.confirmImage:str = options.imagePath + "control/confirmButton.jpg"
        self.energyImage:str = options.energyType.energyImgPath
        self.maxEnergy:str = options.imagePath + "control/maxEnergy.jpg"
        self.restoreImage:str = options.imagePath + "control/RestoreButton.jpg"
        self.close:str = options.imagePath + "control/closeButton.jpg"
        
    def run(self):
        print("This is the no energy Menu")
        time.sleep(self.WAITTIME)

        #Find Image with the energy type
        buttonX, buttonY = self.findImage(self.energyImage, 0.7)
        self.clickOnImage(buttonX, buttonY)

        buttonX, buttonY = self.findImage(self.confirmImage)
        self.clickOnImage(buttonX,buttonY)
        
        time.sleep(1)

        buttonX, buttonY = self.findImage(self.maxEnergy)
        self.clickOnImage(buttonX,buttonY)

        buttonX, buttonY = self.findImage(self.restoreImage)
        self.clickOnImage(buttonX, buttonY)

        time.sleep(1)

        buttonX, buttonY = self.findImage(self.close)
        self.clickOnImage(buttonX, buttonY)

        # Import here to avoid circular import
        from model.screens.edit_gear_menu import EditGearMenu
        EditGearMenu(self.options).run()
