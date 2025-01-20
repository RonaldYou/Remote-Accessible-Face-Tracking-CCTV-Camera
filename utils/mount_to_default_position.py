from gpiozero import PWMOutputDevice
from time import sleep

servo1 = PWMOutputDevice(17, frequency = 50)
servo2 = PWMOutputDevice(27, frequency = 50) #base


print("moving to base position")
#servo1.value = 0.061 #mid
servo1.value = 0.11#max value on mount
servo2.value = 0.062
sleep(0.5)
servo1.off()
servo2.off()
sleep(1.5)

