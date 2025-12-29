"""
Sensor Fusion Module
--------------------
Provides classes for sensor data fusion, primarily using Kalman Filters
to estimate state variables (e.g., altitude, velocity) from noisy measurements.

Author: Bahattin Yunus Çetin
License: MIT
"""

import numpy as np

class SimpleKalmanFilter:
    """
    A basic 1D Kalman Filter implementation.

    This filter is designed for single-variable tracking (e.g., altitude)
    where the state transition model is identity.

    Attributes:
        q (float): Process noise covariance (trust in the model).
        r (float): Measurement noise covariance (trust in the sensor).
        x (float): Estimated value (state).
        p (float): Estimation error covariance.
        k (float): Kalman gain.
    """
    
    def __init__(self, process_variance: float, measurement_variance: float, initial_value: float = 0.0):
        """
        Initialize the Kalman Filter.

        Args:
            process_variance (float): Expected variance in the process (Q).
            measurement_variance (float): Expected variance in measurements (R).
            initial_value (float, optional): Initial estimate of the state. Defaults to 0.0.
        """
        self.q = process_variance
        self.r = measurement_variance
        self.x = initial_value
        self.p = 1.0  # Initial error covariance
        self.k = 0.0  # Initial Kalman gain

    def update(self, measurement: float) -> float:
        """
        Updates the filter with a new measurement calculation.

        Args:
            measurement (float): The latest raw sensor reading.

        Returns:
            float: The filtered (estimated) value.
        """
        # prediction update (Time Update)
        # X_predict = X_prev (Identity model)
        # P_predict = P_prev + Q
        self.p = self.p + self.q

        # measurement update (Measurement Update)
        # K = P_predict / (P_predict + R)
        self.k = self.p / (self.p + self.r)
        
        # X_new = X_predict + K * (Z - X_predict)
        self.x = self.x + self.k * (measurement - self.x)
        
        # P_new = (1 - K) * P_predict
        self.p = (1 - self.k) * self.p

        return self.x

if __name__ == "__main__":
    # Test suite for the Kalman Filter
    print("Testing Linear Kalman Filter...")
    kf = SimpleKalmanFilter(process_variance=0.01, measurement_variance=0.1, initial_value=100.0)
    measurements = [100.2, 100.5, 99.8, 101.0, 99.5]
    
    for i, m in enumerate(measurements):
        filtered = kf.update(m)
        print(f"Step {i+1}: Measured={m:<6.2f} | Filtered={filtered:<6.2f}")

