from model.screens.menu_screen import MenuScreen
from model.screens.training import Training
import time
import pygetwindow as pw

class Controller:
    window = "BlueStacks App Player"

    def __init__(self):
        pass

    def getWindowCenter(self, top, left, width, height):
        centerX = left + height/2
        centerY = top + width/2

        return centerX, centerY

    def startTraining(self,options):
        #size(width=544, height=934)
        blueLockGame = pw.getWindowsWithTitle(self.window)[0]
        time.sleep(0.5)
        blueLockGame.activate()
        blueLockGame.resizeTo(544,934)
        
        centerX, centerY = self.getWindowCenter(blueLockGame.top, blueLockGame.left, blueLockGame.width, blueLockGame.height)
        print(centerX, centerY)
        options.setCenterOfScreen(centerX, centerY)
        
        time.sleep(0.5)
        for i in range(options.numTrain.numTrains):
            print("Training number:", i+1)
            #Training(options).run()
            MenuScreen(options).run()