from model.NumTrains import NumTrains
from model.Player import Player
from model.EnergyType import EnergyType

class TrainingOptions():
    imagePath = "img/"

    def __init__(self, numTrain, player, energyType):
        self.numTrain:NumTrains = numTrain
        self.player:Player = player
        self.energyType:EnergyType = energyType

    def setCenterOfScreen(self, centerX, centerY):
        self.centerX = centerX
        self.centerY = centerY