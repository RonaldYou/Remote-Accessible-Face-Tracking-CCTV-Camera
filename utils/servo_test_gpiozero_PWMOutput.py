from gpiozero import PWMOutputDevice
from time import sleep

servo1 = PWMOutputDevice(17, frequency = 50)
servo2 = PWMOutputDevice(27, frequency = 50) #base

#sleep(5)

print("moving 1")
#servo1.value = 0.025 #max val
servo1.value = 0.03 #min value on mount
servo2.value = 0.025
sleep(0.5)
print(servo1.value)
servo1.off()
servo2.off()
sleep(1.5)


print("moving 2")
#servo1.value = 0.061 #mid
servo1.value = 0.11#max value on mount
servo2.value = 0.062
sleep(0.5)
servo1.off()
servo2.off()
sleep(1.5)

print("moving 3")
#servo1.value = 0.11 #min
servo2.value = 0.12
sleep(0.5)
servo1.off()
servo2.off()
sleep(1.5) 