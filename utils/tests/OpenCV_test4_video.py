import cv2
import libcamera
import pathlib

from picamera2 import Picamera2

cv2.startWindowThread()

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (2304, 1296)}))

picam2.set_controls({'HdrMode': libcamera.controls.HdrModeEnum.SingleExposure})
picam2.start()

cascade_path = pathlib.Path(cv2.__file__).parent.absolute() / "data/haarcascade_frontalface_default.xml"
print(cascade_path)

faceCascade = cv2.CascadeClassifier(str(cascade_path))

while True:
    frame = picam2.capture_array()
    # Convert XRGB to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2RGB)

    # Convert RGB to grayscale
    gray = cv2.cvtColor(rgb_frame, cv2.COLOR_RGB2GRAY)

    faces = faceCascade.detectMultiScale(gray, scaleFactor = 1.1, minNeighbors = 15)

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.putText(frame, "FACE",(x,y-10),cv2.FONT_HERSHEY_COMPLEX, 0.6, (0,255,0),1)
    cv2.imshow("Camera", frame)
    if cv2.waitKey(1) == ord('q'):
        break
    

