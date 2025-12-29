"""
PID Controller Module for Vertical Descent
------------------------------------------
Implements a standard PID control loop for regulating the rocket's
descent velocity during the final landing approach.

Author: Bahattin Yunus Çetin
License: MIT
"""

class PIDController:
    """
    A Proportional-Integral-Derivative (PID) controller.

    Attributes:
        kp (float): Proportional gain.
        ki (float): Integral gain.
        kd (float): Derivative gain.
        integral (float): Accumulated error over time.
        prev_error (float): Error value from the previous step.
    """
    
    def __init__(self, kp: float, ki: float, kd: float):
        """
        Initializes the PID controller with gain coefficients.

        Args:
            kp (float): Proportional gain.
            ki (float): Integral gain.
            kd (float): Derivative gain.
        """
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.integral = 0.0
        self.prev_error = 0.0

    def update(self, setpoint: float, measurement: float, dt: float) -> float:
        """
        Computes the control output based on the current error.

        Args:
            setpoint (float): The desired target value.
            measurement (float): The current measured value.
            dt (float): Time step in seconds.

        Returns:
            float: The calculated control output.
        """
        error = setpoint - measurement
        self.integral += error * dt
        
        # Prevent integral windup (simple clamping could be added here if needed)
        
        if dt > 0:
            derivative = (error - self.prev_error) / dt
        else:
            derivative = 0.0
            
        output = (self.kp * error) + (self.ki * self.integral) + (self.kd * derivative)
        
        self.prev_error = error
        return output

if __name__ == "__main__":
    # Example usage for vertical speed control during touch-down
    print("Initializing PID Controller Module...")
    controller = PIDController(kp=1.5, ki=0.1, kd=0.5)
    print("PID Controller initialized successfully.")

