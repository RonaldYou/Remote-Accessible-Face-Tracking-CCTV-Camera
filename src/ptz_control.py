from gpiozero import PWMOutputDevice
from time import sleep
from queue import Queue

# Constants for PWM duty cycle range
BASE_DUTY_MIN, BASE_DUTY_MAX = 0.03, 0.13
ELEVATION_DUTY_MIN, ELEVATION_DUTY_MAX = 0.03, 0.11
DUTY_CYCLE_PER_DEGREE = (0.1 - 0.01) / 180  # For 180° range

class PTZ:
    """
    PTZ (Pan-Tilt-Zoom) control class for servo-based camera system using PWM.
    """

    def __init__(self, base_pin: int, elevation_pin: int, initial_base_dc: float, initial_elevation_dc: float):
        self.base = PWMOutputDevice(base_pin, frequency=50)
        self.elevation = PWMOutputDevice(elevation_pin, frequency=50)
        self.current_base_dc = initial_base_dc
        self.current_elevation_dc = initial_elevation_dc

        self._apply_pwm(self.current_base_dc, self.current_elevation_dc)
        self._shutdown_servos()

    def _clamp(self, value: float, min_val: float, max_val: float) -> float:
        return max(min_val, min(value, max_val))

    def _apply_pwm(self, base_dc: float, elevation_dc: float):
        self.base.value = base_dc
        self.elevation.value = elevation_dc
        sleep(0.5)  # Servo response time (can be made dynamic)
    
    def _shutdown_servos(self):
        self.base.off()
        self.elevation.off()
        sleep(0.1)

    def move(self, base_angle: float, elevation_angle: float):
        """
        Moves the base and elevation by the given angles in degrees.
        Angles can be positive or negative relative to current orientation.
        """
        print(f"[PTZ] Requested move: base={base_angle:.2f}°, elevation={elevation_angle:.2f}°")

        new_base_dc = self._clamp(
            round(self.current_base_dc + base_angle * DUTY_CYCLE_PER_DEGREE, 3),
            BASE_DUTY_MIN, BASE_DUTY_MAX
        )
        new_elevation_dc = self._clamp(
            round(self.current_elevation_dc + elevation_angle * DUTY_CYCLE_PER_DEGREE, 3),
            ELEVATION_DUTY_MIN, ELEVATION_DUTY_MAX
        )

        print(f"[PTZ] Moving base from {self.current_base_dc:.3f} → {new_base_dc:.3f}, "
              f"elevation from {self.current_elevation_dc:.3f} → {new_elevation_dc:.3f}")

        self._apply_pwm(new_base_dc, new_elevation_dc)
        self._shutdown_servos()

        self.current_base_dc = new_base_dc
        self.current_elevation_dc = new_elevation_dc

def PTZControl(ptz: PTZ, q: Queue, frame_w: int, frame_h: int):
    """
    Continuously consumes face center coordinates from a queue and moves
    the PTZ camera to keep the face centered in the frame.
    """
    DEGREE_PER_PIXEL_W = 45 / 1152  # Horizontal FOV
    DEGREE_PER_PIXEL_H = 15 / 648   # Vertical FOV

    H_THRESHOLD = 250
    V_THRESHOLD = 100

    print("[PTZ] Control loop started...")

    while True:
        centre_x, centre_y = q.get()

        if (centre_x, centre_y) == (-1, -1):
            continue  # No face detected

        dx = centre_x - (frame_w / 2)
        dy = centre_y - (frame_h / 2)

        if abs(dx) <= H_THRESHOLD and abs(dy) <= V_THRESHOLD:
            continue  # Ignore minor jitter

        move_base = DEGREE_PER_PIXEL_W * dx if abs(dx) > H_THRESHOLD else 0
        move_elevation = DEGREE_PER_PIXEL_H * dy if abs(dy) > V_THRESHOLD else 0

        ptz.move(move_base, move_elevation)
