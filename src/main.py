from ptz_control import PTZ
from camera import CameraControl
#import cv2
import threading
from time import sleep


if __name__ == "__main__":
    ptz = PTZ(27,17,0.062,0.11)
    camThread = threading.Thread(target=CameraControl)
    camThread.start()
    

    ptz.move(0, -25)
    sleep(1)
    ptz.move(50, 0)
    sleep(1)
    ptz.move(-50, 0)
    