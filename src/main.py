from ptz_control import PTZ
from camera import CAM
import cv2

def setup():
    ptz = PTZ(27,17,0.062,0.11)
    cam = CAM()


if __name__ == "__main__":
    setup()   