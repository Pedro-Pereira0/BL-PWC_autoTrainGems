from screens.Screen import MenuScreen
import time
import pygetwindow as pw
from util.util import Util
import threading

playerToTrain = "testFiles/teste1(Kunigami).jpg"
window = "BlueStacks App Player"
imagePath = "img/"
util =  Util()

listener_thread = threading.Thread(target=util.exitIfKeyPressed)
listener_thread.daemon = True  # Thread exits when main program ends
listener_thread.start()

TRAININGS = 20

#size(width=544, height=934)
blueLockGame = pw.getWindowsWithTitle(window)[0]
time.sleep(0.5)
blueLockGame.activate()
blueLockGame.resizeTo(544,934)
time.sleep(0.5)
for i in range(TRAININGS):
    print("Training number:", i+1)
    MenuScreen(imagePath).run()


