from view.View import View
from util.Util import Util
import threading

listener_thread = threading.Thread(target=Util.exitIfKeyPressed)
listener_thread.daemon = True 
listener_thread.start()

View().startTraining()