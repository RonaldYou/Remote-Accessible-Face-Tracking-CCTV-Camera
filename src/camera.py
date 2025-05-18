from picamera2 import Picamera2, Preview
from libcamera import *
from queue import Queue
import cv2

picam2 = Picamera2()

class CAM:
    """
    Camera class for capturing frames and detecting faces using OpenCV and PiCamera2.
    """
    
    def __init__(self):
        mode = picam2.sensor_modes[1]
        picam2.video_configuration.transform = Transform(vflip=True)
        picam2.video_configuration.sensor.output_size = mode['size']
        picam2.video_configuration.main.size = mode['size']
        picam2.video_configuration.main.format = 'XRGB8888'
        picam2.video_configuration.sensor.bit_depth = mode['bit_depth']
        print(mode['size'])
        picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous})
        picam2.configure("video")
        print(picam2.camera_configuration())
        picam2.start()
        self.face_cascade = cv2.CascadeClassifier('/home/ronald/Documents/CCTV Camera/utils/assets/haarcascade_frontalface_default.xml')
        
    def detect(self, frame):
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = self.face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 15)
        centreX = centreY = -1
        if(len(faces) > 0):
            x,y,w,h = faces[0]
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            centreX, centreY = x + w/2, y + h/2
            cv2.putText(frame, f"FACE | Centre: {centreX}, {centreY}",(x,y-10),cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,255,0),1)
        return frame, centreX, centreY
        
        
def CameraControl(cam: CAM, q: Queue):
    """
    Continuously captures frames, detects faces, and sends their center to the queue.
    Displays the annotated video stream in a window.
    """
    while True:
        frame = picam2.capture_array("main")
        frame, centreX, centreY = cam.detect(frame)
        q.put((centreX, centreY))
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) == ord('q'):
            break
