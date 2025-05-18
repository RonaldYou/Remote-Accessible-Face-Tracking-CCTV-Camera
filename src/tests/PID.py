import time
import matplotlib.pyplot as plt

class PIDController:
    def __init__(self, kp, ki, kd, setpoint):
        self.kp = kp  # Proportional gain
        self.ki = ki  # Integral gain
        self.kd = kd  # Derivative gain
        self.setpoint = setpoint  # Desired value
        self.integral = 0  # Cumulative error
        self.previous_error = 0  # Previous error for derivative calculation

    def compute(self, current_value, dt):
        # Calculate error
        error = self.setpoint - current_value

        # Calculate proportional, integral, and derivative terms
        self.integral += error * dt
        derivative = (error - self.previous_error) / dt

        # Calculate PID output
        output = (self.kp * error) + (self.ki * self.integral) + (self.kd * derivative)

        # Update previous error
        self.previous_error = error

        return output

# Simulated system: Heating a room
class SimulatedSystem:
    def __init__(self, initial_temp):
        self.temperature = initial_temp

    def update(self, power, dt):
        # Simulate heating (power adds heat, room loses heat over time)
        self.temperature += power * dt - 0.1 * (self.temperature - 20) * dt  # Cooling to ambient (20°C)
        return self.temperature

# Main function
if __name__ == "__main__":
    # PID parameters
    kp, ki, kd = 2.0, 0.5, 0.1
    setpoint = 75  # Target temperature in degrees Celsius

    pid = PIDController(kp, ki, kd, setpoint)
    system = SimulatedSystem(initial_temp=20)  # Start at room temperature

    # Simulation parameters
    dt = 0.1  # Time step in seconds
    time_duration = 30  # Total simulation time in seconds
    steps = int(time_duration / dt)

    # Data for visualization
    times = []
    temperatures = []
    setpoints = []

    for step in range(steps):
        current_time = step * dt
        current_temp = system.temperature

        # Compute PID output and update system
        power = pid.compute(current_temp, dt)
        system.update(power, dt)

        # Store data for plotting
        times.append(current_time)
        temperatures.append(current_temp)
        setpoints.append(setpoint)

        time.sleep(dt)  # Simulate real-time

    # Plot results
    plt.figure(figsize=(10, 5))
    plt.plot(times, temperatures, label="Temperature (°C)")
    plt.plot(times, setpoints, label="Setpoint (°C)", linestyle="--")
    plt.title("PID Temperature Control Simulation")
    plt.xlabel("Time (s)")
    plt.ylabel("Temperature (°C)")
    plt.legend()
    plt.grid()
    plt.show()