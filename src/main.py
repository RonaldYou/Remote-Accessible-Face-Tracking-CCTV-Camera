from ptz_control import PTZControl, PTZ
from camera import CameraControl, CAM
import threading
from time import sleep
from queue import Queue

FRAME_W = 2304
FRAME_H = 1296

if __name__ == "__main__":
    ptz = PTZ(27,17,0.062,0.11)
    cam = CAM()
    
    coordQ = Queue()
    
    ptzThread = threading.Thread(target=PTZControl, args=(ptz,coordQ, FRAME_W, FRAME_H))
    camThread = threading.Thread(target=CameraControl, args=(cam,coordQ))
    
    
    ptzThread.start()
    camThread.start()
    
    
    