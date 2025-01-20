import cv2
from picamera2 import Picamera2, Preview
from libcamera import *

def setup(picam2):
    mode = picam2.sensor_modes[1]
    picam2.video_configuration.transform = Transform(vflip=True)
    picam2.video_configuration.sensor.output_size = mode['size']
    picam2.video_configuration.main.size = mode['size']
    picam2.video_configuration.main.format = 'XRGB8888'
    picam2.video_configuration.sensor.bit_depth = mode['bit_depth']
    print(mode['size'])
    #picam2.video_configuration.controls.FrameRate = mode['fps']
    picam2.set_controls({"AfMode": controls.AfModeEnum.Continuous})
    picam2.configure("video")
    print(picam2.camera_configuration())
    picam2.start()

if __name__ == "__main__":
    picam2 = Picamera2()
    setup(picam2)
    face_cascade = cv2.CascadeClassifier('/home/ronald/Documents/CCTV Camera/utils/assets/haarcascade_frontalface_default.xml')
    while True:
        frame = picam2.capture_array("main")
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 15)
        for (x,y,w,h) in faces:
            cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
            cv2.putText(frame, f"FACE | Centre: {x + w/2}, {y + h/2}",(x,y-10),cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,255,0),1)
        cv2.imshow("Camera", frame)
        if cv2.waitKey(1) == ord('q'):
            break

