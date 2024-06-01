import cv2
import numpy
import libcamera
from flask import Flask, render_template, Response, stream_with_context, request
from picamera2 import Picamera2

picam2 = Picamera2()
picam2.configure(picam2.create_preview_configuration(main={"format": 'XRGB8888', "size": (640, 480)}))

#picam2.set_controls({'HdrMode': libcamera.controls.HdrModeEnum.SingleExposure})
picam2.start()

app = Flask('__name__')

def video_stream():
    while True:
        frame = picam2.capture_array()
        _, buffer = cv2.imencode('.jpeg',frame, [int(cv2.IMWRITE_JPEG_QUALITY), 70]) #compressing more
        frame = buffer.tobytes()
        yield (b'--frame\r\n' b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n\r\n')

@app.route('/camera')
def camera():
    return render_template('camera.html')

@app.route('/video_feed')
def video_feed():
    return Response(video_stream(), mimetype='multipart/x-mixed-replace; boundary=frame')

app.run(host='0.0.0.0', port='5000', debug=False)