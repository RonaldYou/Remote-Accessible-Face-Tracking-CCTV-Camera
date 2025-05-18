from gpiozero import PWMOutputDevice #15.2.2 in documentation
from time import sleep

DUTY_CYCLE_PER_DEGREE = (0.1 - 0.01)/180

class PTZ:
    def __init__(self, basePin, eUnitPin, initialBaseDC, initialeUnitDC):
        self.base = PWMOutputDevice(basePin, frequency = 50)
        self.eUnit = PWMOutputDevice(eUnitPin, frequency = 50)
        self.currentBaseDC = initialBaseDC
        self.currenteUnitDC = initialeUnitDC
        self.base.value = self.currentBaseDC
        self.eUnit.value = self.currenteUnitDC
        sleep(0.5) #make dynamic?
        self.base.off()
        self.eUnit.off()
        sleep(0.1)
        
    def move(self, baseAngle, elevationAngle):
        # 180 degrees is from 0.01 to 0.1
        #eUnit (elevation unit):
        #	min value: 0.03
        #	max value: 0.11
        #	less than 180 degrees
        #base:
        #	min value: 0.03
        #	max value: 0.13
        #	full 180 degrees
        sleep(0.5)
        print(f"Moving base by {baseAngle} degrees and elevation by {elevationAngle}")
        newBaseDC = round(self.currentBaseDC + baseAngle * DUTY_CYCLE_PER_DEGREE,3)
        neweUnitDC = round(self.currenteUnitDC + elevationAngle * DUTY_CYCLE_PER_DEGREE,3)
        print(f"Moving base from {self.currentBaseDC} to  {newBaseDC}, moving e from {self.currenteUnitDC} to {neweUnitDC}")
        self.base.value = newBaseDC
        self.eUnit.value = neweUnitDC
        
        sleep(0.5)
        self.base.off()
        self.eUnit.off()
        
        self.currentBaseDC = newBaseDC
        self.currenteUnitDC = neweUnitDC
        
        
        
def PTZControl(ptz, q, frame_w, frame_h):
    #width: 1152 pixels per 45 degrees
    DEGREE_PER_PIXEL_W = 45/1152
    DEGREE_PER_PIXEL_H = 0
    OLD_X = -1
    OLD_Y = -1
    
    while True:
        centreX, centreY = q.get()
        if(centreX == -1 or centreY == -1):
            continue
        #check distance from OLD detection
        if(abs(sqrt(centreX**2 + centreY**2) - sqrt(OLD_X**2 + OLD_Y**2)) <= 100):
            continue
        
        
        
        #ptz
    



