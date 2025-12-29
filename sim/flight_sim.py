"""
Vertical Landing Simulation
---------------------------
Simulates the physics and control loop of a vertical landing rocket.
Demonstrates the integration of PID control, Sensor Fusion, and Telemetry.

Run: python sim/flight_sim.py

Author: Bahattin Yunus Çetin
"""

import sys
import os
import time
import numpy as np

# Add src to path to import local modules
sys.path.append(os.path.join(os.path.dirname(__file__), '..', 'src'))

from controller import PIDController
from sensor_fusion import SimpleKalmanFilter
from telemetry import TelemetryPacket

def print_header():
    print(r"""
    ================================================================
       VERTICAL-ARCH | MISSION CONTROL CENTER | FLIGHT SIMULATION
    ================================================================
    """)

def run_simulation():
    # Simulation parameters
    dt = 0.1
    duration = 60.0
    gravity = -9.81
    mass = 2.0  # kg
    max_thrust = 40.0  # N

    # Initial state
    altitude = 150.0  # meters
    velocity = -5.0   # initial descent m/s
    thrust = 0.0

    # Initialize Modules
    pid = PIDController(kp=25.0, ki=2.0, kd=15.0)
    kf = SimpleKalmanFilter(process_variance=0.1, measurement_variance=0.5, initial_value=altitude)
    
    # Target: Soft touchdown at 0 meters
    target_altitude = 0.0

    print_header()
    print(f"{'TIME (s)':<10} | {'ALT (m)':<10} | {'VEL (m/s)':<10} | {'THRUST (N)':<10} | {'STATUS':<15}")
    print("-" * 75)

    success = False
    
    for t in np.arange(0, duration, dt):
        # 1. SENSOR Read & Fusion (Simulating noise)
        noise = np.random.normal(0, 0.2)
        measured_alt = altitude + noise
        est_alt = kf.update(measured_alt)
        
        # 2. CONTROL Logic
        # Descent logic: We want velocity to be proportional to height (safe approach)
        # v_target = -sqrt(2 * a * h) is standard for constant deceleration, 
        # but here we use a simple linear approach for stability test.
        # We clamp the target velocity to not exceed -20 m/s (terminal velocity check)
        
        if est_alt > 10.0:
            target_velocity = -5.0 # Constant descent speed until close
        else:
            target_velocity = -1.0 # Slow down for touchdown
            
        # If we are effectively on ground
        if altitude <= 0.1 and abs(velocity) < 1.0:
            altitude = 0.0
            velocity = 0.0
            print(f"{t:<10.1f} | {altitude:<10.2f} | {velocity:<10.2f} | {0.0:<10.2f} | {'TOUCHDOWN':<15}")
            print("\n>>> MISSION SUCCESS: SMOOTH LANDING CONFIRMED.")
            success = True
            break
            
        if altitude < 0:
            print(f"\n>>> CRITICAL FAILURE: IMPACT VELOCITY {velocity:.2f} m/s")
            break

        # Calculate Thrust
        thrust_demand = pid.update(target_velocity, velocity, dt)
        
        # Gravity compensation + PID output
        thrust = np.clip(thrust_demand + (mass * -gravity), 0, max_thrust)

        # 3. PHYSICS Update
        accel = (thrust / mass) + gravity
        velocity += accel * dt
        altitude += velocity * dt
        
        # 4. TELEMETRY (Sample output)
        if int(t * 10) % 5 == 0: # Print every 0.5s
            status_code = 1 # In-Flight
            packet = TelemetryPacket(altitude, velocity, accel, status_code)
            # pseudo-send packet.pack()
            print(f"{t:<10.1f} | {altitude:<10.2f} | {velocity:<10.2f} | {thrust:<10.2f} | {'DESCENDING'}")

    if not success and altitude > 0:
        print("\n>>> TIMEOUT: Fuel exhausted or simulation ended before landing.")

if __name__ == "__main__":
    run_simulation()

