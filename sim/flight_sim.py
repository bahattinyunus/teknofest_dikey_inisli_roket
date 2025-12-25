import sys
import os
import time
import numpy as np

# Add src to path to import PIDController
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))
from controller import PIDController

def run_simulation():
    # Simulation parameters
    dt = 0.1
    duration = 20.0
    gravity = -9.81
    mass = 2.0  # kg
    max_thrust = 40.0  # N

    # Initial state
    altitude = 100.0  # meters
    velocity = 0.0
    thrust = 0.0

    # PID Settings (Tuned for soft landing)
    # Goal: Control altitude descent towards 0
    controller = PIDController(kp=25.0, ki=2.0, kd=15.0)
    target_altitude = 0.0

    print("--- Vertical Landing Simulation Start ---")
    print(f"{'Time':<10} {'Alt':<10} {'Vel':<10} {'Thrust':<10}")

    for t in np.arange(0, duration, dt):
        if altitude <= 0.1 and abs(velocity) < 0.5:
            altitude = 0
            print(f"{t:<10.1f} {altitude:<10.2f} {velocity:<10.2f} {thrust:<10.2f}")
            print("--- Touchdown! ---")
            print(f"Final Velocity: {velocity:.2f} m/s")
            print("SUCCESS: Soft Landing Secured.")
            break
        
        if altitude < 0:
             print(f"--- Crash at {velocity:.2f} m/s ---")
             break

        # PID controls thrust based on ALTITUDE error
        # We want to maintain a controlled descent velocity that decreases as we get near ground
        v_target = -np.sqrt(2 * 0.5 * max(0.1, altitude)) # Simple square root control law for smooth descent
        thrust_demand = controller.update(v_target, velocity, dt)
        
        thrust = np.clip(thrust_demand + (mass * -gravity), 0, max_thrust)

        # Physics update
        accel = (thrust / mass) + gravity
        velocity += accel * dt
        altitude += velocity * dt

        if int(t * 10) % 10 == 0:
            print(f"{t:<10.1f} {altitude:<10.2f} {velocity:<10.2f} {thrust:<10.2f}")

if __name__ == "__main__":
    run_simulation()
