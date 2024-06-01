from gpiozero import Servo
from time import sleep
from gpiozero.pins.pigpio import PiGPIOFactory

factory = PiGPIOFactory()

servo = Servo(11, pin_factory=factory)

servo.min()
sleep(2)

servo.mid()
sleep(2)

servo.max()
sleep(2)