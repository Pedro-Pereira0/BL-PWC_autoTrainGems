import pyautogui as pg
import time
from opencv.Opencv import getTextFromImage

class Screen:
    def __init__(self, imagePath):
       self.imagePath = imagePath
       self.WAITTIME = 2
       

    def run(self):
        print("Iam running")

    def findImage(self,image, confValue = 0.8):
        try:
            buttonX, buttonY = pg.locateCenterOnScreen(image, confidence=confValue, grayscale=True)
            return buttonX, buttonY
        except pg.ImageNotFoundException:
            print("Image not found! Image:", image)
            return None,None
        
    def findImageForScreenShot(self,image, confValue = 0.8):
        try:
            imageLoc = pg.locateOnScreen(image, confidence=confValue)
            return imageLoc
        except pg.ImageNotFoundException:
            print("Image not found! Image:", image)
            return None
        
    def clickOnImage(self, clickX, clickY, interval = 0.5):
        if(clickX != None and clickY != None):
            time.sleep(interval)
            pg.click(clickX, clickY)
            time.sleep(interval)
        else: 
            print("Cannot click invalid coordinates")
    
    #Alguns valores alterados por causa de ser uma imagem especifica
    def convertToIntTuple(self, position):
        left = int(position.left)+ 100
        top = int(position.top)
        height = int(position.height)
        width = int(position.width)+50

        return (left,top,width,height)
    
    #Este metodo vai tratar da string (tirar espaços em branco e criar uma substring) e retornar apenas 
    # a energia depois do treino
    def stringTreatment(self, string):
        string.strip()
        list = string.rsplit(">")
        return list[1]
    
class MenuScreen(Screen):
    def __init__(self, imagePath):
        super().__init__(imagePath)
        self.trainImg = imagePath+"control/train.jpg"

    def run(self):
        print("This is the Menu Screen")
        time.sleep(self.WAITTIME)
        buttonX, buttonY = self.findImage(self.trainImg)
        self.clickOnImage(buttonX, buttonY)
        TrainingMenuScreen(self.imagePath).run()

class TrainingMenuScreen(Screen):
    def __init__(self, imagePath):
        super().__init__(imagePath)
        self.typeTrain = imagePath + "control/typeTrain.jpg"
        self.prevTrain = imagePath + "control/leftSideButton.jpg"
        self.nextImg = imagePath + "control/nextButton.jpg"

    def run(self):
        print("This is the Training Menu Screen")
        time.sleep(self.WAITTIME)
        while True:
            buttonX, buttonY = self.findImage(self.typeTrain)
            time.sleep(0.5)
            if buttonX == None or buttonY == None:
                button1X, button1Y = self.findImage(self.prevTrain)
                self.clickOnImage(button1X, button1Y)
            else:
                break

        button2X, button2Y = self.findImage(self.nextImg)
        self.clickOnImage(button2X, button2Y)

        SelectPlayerScreen(self.imagePath).run()

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

        EditSupportScreen(self.imagePath).run()

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

        FriendChooseMenu(self.imagePath).run()
        print("Back")
        time.sleep(2)

        buttonX, buttonY = self.findImage(self.nextButton)
        self.clickOnImage(buttonX,buttonY)

        EditGearMenu(self.imagePath).run()

class FriendChooseMenu(Screen):
    def __init__(self,imagePath):
        super().__init__(imagePath)
        self.confirm = imagePath + "control/confirmButton.jpg"

    def run(self):
        print("This is the Friend Choose Menu")
        time.sleep(self.WAITTIME)

        buttonX, buttonY = self.findImage(self.confirm)
        self.clickOnImage(buttonX,buttonY)

class EditGearMenu(Screen):
    def __init__(self,imagePath):
        super().__init__(imagePath)
        self.nextImage = imagePath + "control/nextButton.jpg"

    def run(self):
        print("This is the Edit Gear Menu")
        time.sleep(self.WAITTIME)

        buttonX, buttonY = self.findImage(self.nextImage)
        self.clickOnImage(buttonX,buttonY)
        
        FinalConfirmationMenu(self.imagePath).run()

class FinalConfirmationMenu(Screen):
    def __init__(self,imagePath):
        super().__init__(imagePath)
        self.startTrainButton = imagePath + "control/startTrainButton.jpg"
        self.energyImg = imagePath + "control/energyImg.jpg"
    def run(self):
        print("This is the Final Confirmation")
        time.sleep(self.WAITTIME)
        #Get The stamina value after the training
        energyLoc = self.findImageForScreenShot(self.energyImg)
        #Adds width because i want to extract the energy left
        region = self.convertToIntTuple(energyLoc)
        staminaImg = pg.screenshot(region = region)
    
        energy = getTextFromImage(staminaImg)

        energyLeftString = self.stringTreatment(energy)
        
        energyLeft = int(energyLeftString)
        print(energyLeft)
        isThereEnergy = True
        if(energyLeft < 0):
            print("No energy left!")
            isThereEnergy = False       
        
        buttonX, buttonY = self.findImage(self.startTrainButton)
        self.clickOnImage(buttonX,buttonY)
        
        if isThereEnergy == True:
            Training(self.imagePath).run()
        else:
            NoEnergyMenu(self.imagePath).run()

class Training(Screen):
    def __init__(self,imagePath):
        super().__init__(imagePath)
        self.autoButton = imagePath + "control/autoButton.jpg"
        self.trainCard = imagePath + "control/trainCard.jpg"
        self.training = imagePath + "control/training.jpg"

    def run(self):
        print("Training has started...")
        time.sleep(5)

        buttonX, buttonY = self.findImage(self.autoButton)
        for i in range(5):
            self.clickOnImage(buttonX,buttonY, 0.1)
        
        #It has to end the conversation
        time.sleep(5)

        buttonX, buttonY = self.findImage(self.trainCard, 0.4)

        isTraining = True
        while isTraining == True:
            self.clickOnImage(buttonX, buttonY, interval = 0.2)
            self.clickOnImage(buttonX, buttonY, interval = 0.2)

            button1X, button1Y = self.findImage(self.training)
            if(button1X == None or button1Y == None):
                time.sleep(1)
                button1X, button1Y = self.findImage(self.training)
                if(button1X == None or button1Y == None):
                    isTraining = False
                    EndTrain(self.imagePath).run()

class EndTrain(Screen):
    def __init__(self,imagePath):
        super().__init__(imagePath)
        self.finishButton = imagePath + "control/finishButton.jpg"
        self.cancelButton = imagePath + "control/cancelButton.jpg"
    def run(self):
        print("This is the End Training Menu")
        time.sleep(self.WAITTIME)

        buttonX, buttonY = self.findImage(self.finishButton)
        self.clickOnImage(buttonX,buttonY)

        time.sleep(3)

        self.clickOnImage(buttonX, buttonY)

        time.sleep(5)

        self.clickOnImage(buttonX, buttonY)
        self.clickOnImage(buttonX, buttonY)

        buttonX, buttonY = self.findImage(self.cancelButton)
        self.clickOnImage(buttonX, buttonY)
        time.sleep(8)


class NoEnergyMenu(Screen):
    def __init__(self,imagePath):
        super().__init__(imagePath)
        self.confirmImage = imagePath + "control/confirmButton.jpg"
        self.maxEnergy = imagePath + "control/maxEnergy.jpg"
        self.restoreImage = imagePath + "control/RestoreButton.jpg"
        self.close = imagePath + "control/closeButton.jpg"
    def run(self):
        print("This is the no energy Menu")
        time.sleep(self.WAITTIME)

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

        EditGearMenu(self.imagePath).run()