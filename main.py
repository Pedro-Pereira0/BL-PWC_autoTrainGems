from view.View import View
from util.Util import Util
import threading

listener_thread = threading.Thread(target=Util.exitIfKeyPressed)
listener_thread.daemon = True  # Thread exits when main program ends
listener_thread.start()

View().startTraining()

