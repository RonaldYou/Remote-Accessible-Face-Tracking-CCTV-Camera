from gpiozero import Servo
from time import sleep

servo1 = Servo(17, min_pulse_width = 0.0005, max_pulse_width = 0.0025)
servo2 = Servo(27, min_pulse_width = 0.0005, max_pulse_width = 0.0025)

for i in range (10):
    print("moving to position 1")
    servo1.min()
    servo2.max()
    sleep(2)
    print("moving to position 2")
    servo1.mid()
    servo2.mid()
    sleep(2)
    print("moving to position 3")
    servo1.max()
    servo2.min()
    sleep(2)