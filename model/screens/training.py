import time
from model.screens.base_screen import Screen

class Training(Screen):
    def __init__(self,options):
        super().__init__(options)
        self.autoButton:str = options.imagePath + "control/autoButton.jpg"
        self.trainCard:str = options.imagePath + "control/trainCard.jpg"
        self.training:str = options.imagePath + "control/training.jpg"

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

            #Check if its in a match screen, if so, start the match.
            from model.screens.match import Match
            Match(self.options).run()

            #Verify if its still training
            button1X, button1Y = self.findImage(self.training)
            if(button1X == None or button1Y == None):
                time.sleep(1)
                button1X, button1Y = self.findImage(self.training)
                if(button1X == None or button1Y == None):
                    isTraining = False
                    # Import here to avoid circular import
                    from model.screens.end_train import EndTrain
                    EndTrain(self.options).run()