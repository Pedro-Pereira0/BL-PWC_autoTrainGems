class PlayerGrid():
    def __init__(self, screenCenterX, screenCenterY):
        self.screenCenterX = screenCenterX
        self.screenCenterY = screenCenterY
        
        self.row = [self.screenCenterY + 248, self.screenCenterY + 346, self.screenCenterY + 434]

        self.collumn = [self.screenCenterX - 24, self.screenCenterX - 121, self.screenCenterX - 213, 
                         self.screenCenterX - 314, self.screenCenterX - 410]

    