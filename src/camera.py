from picamera2 import Picamera2, Preview
from libcamera import *

picam2 = Picamera2()

class CAM:
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
