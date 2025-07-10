from model.screens.menu_screen import MenuScreen
from model.screens.no_energy_menu import NoEnergyMenu
import time
import pygetwindow as pw

class Controller:
    window = "BlueStacks App Player"

    def __init__(self):
        pass

    def startTraining(self,options):
        #size(width=544, height=934)
        blueLockGame = pw.getWindowsWithTitle(self.window)[0]
        time.sleep(0.5)
        blueLockGame.activate()
        blueLockGame.resizeTo(544,934)
        time.sleep(0.5)
        for i in range(options.numTrain.numTrains):
            print("Training number:", i+1)
            NoEnergyMenu(options).run()
            #MenuScreen(options).run()