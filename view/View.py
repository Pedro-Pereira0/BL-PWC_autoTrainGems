from tkinter import *
from model.NumTrains import NumTrains
from model.Player import Player
from model.TrainingOptions import TrainingOptions

from controller.Controller import Controller

class View:
    def __init__(self):
        self.PADDING = 20

    def startTraining(self):
        window = Tk()
        window.title("BL:PWC AutoTraining Options")
        window.geometry("800x600")

        #columns
        window.columnconfigure(0, weight = 1)
        window.columnconfigure(1,weight = 1)
        window.columnconfigure(2, weight = 1)
        window.columnconfigure(3, weight = 2)

        #rows
        window.rowconfigure(0, weight = 1)
        window.rowconfigure(1, weight = 1)
        window.rowconfigure(2, weight = 1)
        window.rowconfigure(3, weight = 2)

        #Labels
        nTrainingsLabel = Label(window, text = "Number of trainings:")
        nTrainingsLabel.grid(column = 0, row = 0, sticky = "W", padx = self.PADDING, pady = self.PADDING)

        playerLabel = Label(window, text = "Choose player to train:")
        playerLabel.grid(column = 0, row = 1, sticky = "W", padx = self.PADDING, pady = self.PADDING)

        energyTypeLabel = Label(window, text = "Choose the energy type to use:")
        energyTypeLabel.grid (column = 0, row = 2, sticky = "W", padx = self.PADDING, pady = self.PADDING)

        #Inputs
        nTrainingsInput = Entry(window)
        nTrainingsInput.grid(column = 1, row = 0, sticky = "W", padx = self.PADDING, pady = self.PADDING) 
       
        playerList = ["Kunigami","Junichi"]
        playerValue = StringVar(window)
        playerValue.set("Select a player:")

        playerMenu = OptionMenu(window, playerValue, *playerList)
        playerMenu.grid(column = 1, row = 1, sticky = "W", padx = self.PADDING, pady = self.PADDING)

        energyTypeVar = IntVar()
       
        energyTypeSmallRadio = Radiobutton(window, text = "Small", variable = energyTypeVar, value = 0)
        energyTypeSmallRadio.grid(column = 1, row = 2, sticky = "N", padx = self.PADDING, pady = self.PADDING)

        energyTypeMediumRadio = Radiobutton(window, text = "Medium",variable = energyTypeVar, value = 1)
        energyTypeMediumRadio.grid(column = 2, row = 2, sticky = "N", padx = self.PADDING, pady = self.PADDING)

        energyTypeBigRadio = Radiobutton(window, text = "Big",variable = energyTypeVar, value = 2)
        energyTypeBigRadio.grid(column = 3, row = 2, sticky = "N", padx = self.PADDING, pady = self.PADDING)

        def getTrainingOptions():
            try:
                numTrain = NumTrains(nTrainingsInput.get())
                player = Player(playerValue.get())
                energyType = energyTypeVar.get()
                options = TrainingOptions(numTrain, player, energyType)
                
                controller = Controller()
                controller.startTraining(options)

            except Exception as err:
                print("Error:", err)

  
        btnStartTraining = Button(window, text = "Start training" ,fg = "black", command=getTrainingOptions)
        btnStartTraining.grid(column=4, row=4,sticky="SE", padx = self.PADDING, pady= self.PADDING)

        # Execute Tkinter
        window.mainloop()