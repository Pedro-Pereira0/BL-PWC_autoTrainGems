import time
import pyautogui as pg
from model.screens.base_screen import Screen
from model.opencv.Opencv import getTextFromImage

class FinalConfirmationMenu(Screen):
    def __init__(self,options):
        super().__init__(options)
        self.startTrainButton:str = options.imagePath + "control/startTrainButton.jpg"
        self.energyImg:str = options.imagePath + "control/energyImg.jpg"

    def extractEnergy(self, string):
        string.strip()
        if string.count(">") > 1:
            ns = string.replace(">",1)
            list = ns.rsplit(">")
        else:
            list = string.rsplit(">")
        
        return list[1]
        
    def run(self):
        print("This is the Final Confirmation")
        time.sleep(self.WAITTIME)

        while True:
            #Get The stamina value after the training
            energyLoc = self.findImageForscreenshot(self.energyImg)
            #Adds width because i want to extract the energy left
            left, top, width, height = self.convertBoxToInt(energyLoc)
            region = (left + 100, top, width + 50, height)
            
            staminaImg = pg.screenshot(region = region)
        
            energy = getTextFromImage(staminaImg)

            energyLeftString = self.extractEnergy(energy)
            try:
                energyLeft = int(energyLeftString)
                break
            except:
                print("Retry to get the remaining energy...")


        print(energyLeft)
        isThereEnergy = True
        if(energyLeft < 0):
            print("No energy left!")
            isThereEnergy = False       
        
        buttonX, buttonY = self.findImage(self.startTrainButton)
        self.clickOnImage(buttonX,buttonY)
        
        if isThereEnergy == True:
            # Import here to avoid circular import
            from model.screens.training import Training
            Training(self.options).run()
        else:
            # Import here to avoid circular import
            from model.screens.no_energy_menu import NoEnergyMenu
            NoEnergyMenu(self.options).run()