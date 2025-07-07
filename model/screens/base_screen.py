import pyautogui as pg
import time
from model.opencv.Opencv import getTextFromImage

class Screen:
    def __init__(self, options):
       self.options = options
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
        
    def findImageForscreenshot(self,image, confValue = 0.8):
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