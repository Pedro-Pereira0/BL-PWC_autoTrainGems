import time
import pyautogui as pg
from model.screens.base_screen import Screen
from model.opencv.Opencv import getTextFromImage

class FinalConfirmationMenu(Screen):
    def __init__(self,options):
        super().__init__(options)
        self.startTrainButton = options.imagePath + "control/startTrainButton.jpg"
        self.energyImg = options.imagePath + "control/energyImg.jpg"

    #Este metodo vai tratar da string (tirar espaços em branco e criar uma substring) e retornar apenas 
    # a energia depois do treino
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
        #Get The stamina value after the training
        energyLoc = self.findImageForscreenshot(self.energyImg)
        #Adds width because i want to extract the energy left
        region = self.convertToIntTuple(energyLoc)
        staminaImg = pg.screenshot(region = region)
    
        energy = getTextFromImage(staminaImg)

        energyLeftString = self.extractEnergy(energy)
        
        energyLeft = int(energyLeftString)
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