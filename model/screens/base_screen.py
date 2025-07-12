import pyautogui as pg
import time
from model.opencv.Opencv import getTextFromImage
from model.TrainingOptions import TrainingOptions

class Screen:
    def __init__(self, options):
       self.options:TrainingOptions = options
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
    
    def findImageWithRegion(self,image, region ,confValue = 0.8):
        try:
            buttonX, buttonY = pg.locateCenterOnScreen(image, region = region ,confidence=confValue, grayscale=False)
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
        
    def findAllImages(self, img, conf = 0.76) -> list:
        allImages = pg.locateAllOnScreen(img, grayscale=True, confidence = conf)
        return list(allImages)
        
    def clickOnImage(self, clickX, clickY, interval = 0.5):
        if(clickX != None and clickY != None):
            time.sleep(interval)
            pg.click(clickX, clickY)
            time.sleep(interval)
        else: 
            print("Cannot click invalid coordinates")
    
    #Alguns valores alterados por causa de ser uma imagem especifica
    def convertBoxToInt(self, position):
        left = int(position.left)
        top = int(position.top)
        height = int(position.height)
        width = int(position.width)

        return left,top,width,height