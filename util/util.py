import keyboard
import os

class Util:
    def __init__(self):
        pass

    def exitIfKeyPressed(self, key = 'q'):
        print("Key listener thread started.")
        while(True):
            if keyboard.is_pressed(key):  # if key 'q' is pressed 
                print("Program is stopping...")
                os._exit(1)
                break