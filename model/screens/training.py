import time
import pyautogui as pg
from model.screens.base_screen import Screen

class Training(Screen):
    def __init__(self,options):
        super().__init__(options)
        self.autoButton:str = options.imagePath + "control/autoButton.jpg"
        self.trainCard:str = options.imagePath + "control/trainCard.jpg"
        self.training:str = options.imagePath + "control/training.jpg"
        self.playMatchButton:str = options.imagePath + "control/playMatchButton.jpg"
        self.powerfullOpponentInfo:str = options.imagePath + "control/powerfulOpponentInfo.jpg"

    def run(self):
        from model.screens.match import Match
        from model.screens.end_train import EndTrain

        print("Training has started...")
        time.sleep(5)

        buttonX, buttonY = self.findImage(self.autoButton)
        for i in range(5):
            self.clickOnImage(buttonX,buttonY, 0.1)
        
        #It has to end the conversation
        time.sleep(5)

        #Finds the train card. It doesnt work 100%, some cards are not detected.
        # buttonX, buttonY = self.findImage(self.trainCard, 0.4)

        buttonX = self.options.centerX
        buttonY = self.options.centerY + 425

        isTraining = True
        while isTraining == True:
            
            # #Detect powerfull opponent, so the train fails quicker (might not work as entended because units get stronger)
            # button1X, button1Y = self.findImage(self.powerfullOpponentInfo)
            # #Slightly below so it touches the button, could also check if it exists and find the button itself, not worth it for now.
            # if button1X != None and button1Y != None:
            #     self.clickOnImage(button1X, button1Y + 25)
            #     button1X, button1Y = self.findImage(self.playMatchButton)
            #     self.clickOnImage(button1X, button1Y)
            #     Match(self.options).run(True)


            self.clickOnImage(buttonX, buttonY, interval = 0.2)
            self.clickOnImage(buttonX, buttonY, interval = 0.2)

            #Check if its in a match screen, if so, start the match.
            Match(self.options).run()

            #Verify if its still training
            button1X, button1Y = self.findImage(self.training)
            if(button1X == None or button1Y == None):
                time.sleep(1)
                button1X, button1Y = self.findImage(self.training)
                if(button1X == None or button1Y == None):
                    isTraining = False
                    # Import here to avoid circular import
                    EndTrain(self.options).run()