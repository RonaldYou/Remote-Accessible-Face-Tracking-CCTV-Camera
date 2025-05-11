from ptz_control import PTZControl, PTZ
from camera import CameraControl, CAM
import threading
from time import sleep
from queue import Queue


if __name__ == "__main__":
    ptz = PTZ(27,17,0.062,0.11)
    cam = CAM()
    
    coordQ = Queue()
    
    ptzThread = threading.Thread(target=PTZControl, args=(ptz,coordQ))
    camThread = threading.Thread(target=CameraControl, args=(cam,coordQ))
    
    
    ptzThread.start()
    camThread.start()
    
    
    