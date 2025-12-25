import numpy as np

class SimpleKalmanFilter:
    """
    A basic 1D Kalman Filter for altitude tracking using Baro and IMU.
    """
    def __init__(self, process_variance, measurement_variance, initial_value=0):
        self.q = process_variance  # Process noise covariance
        self.r = measurement_variance  # Measurement noise covariance
        self.x = initial_value  # Estimated value
        self.p = 1.0  # Estimation error covariance
        self.k = 0.0  # Kalman gain

    def update(self, measurement):
        # Prediction update
        self.p = self.p + self.q

        # Measurement update
        self.k = self.p / (self.p + self.r)
        self.x = self.x + self.k * (measurement - self.x)
        self.p = (1 - self.k) * self.p

        return self.x

if __name__ == "__main__":
    kf = SimpleKalmanFilter(0.01, 0.1)
    measurements = [100.2, 100.5, 99.8, 101.0, 99.5]
    for m in measurements:
        print(f"Measured: {m}, Filtered: {kf.update(m):.2f}")
