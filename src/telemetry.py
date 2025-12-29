"""
Telemetry Module
----------------
Handles the packing and management of telemetry data packets for
ground station communication.

Author: Bahattin Yunus Çetin
License: MIT
"""

import struct
import time

class TelemetryPacket:
    """
    Defines the data structure for rocket-to-ground communication.
    
    Attributes:
        timestamp (float): UNIX timestamp of packet creation.
        altitude (float): Current altitude in meters.
        velocity (float): Current vertical velocity in m/s.
        acc_z (float): Vertical acceleration in m/s^2.
        status_code (int): System status flag.
    """
    
    def __init__(self, altitude: float, velocity: float, acc_z: float, status_code: int):
        """
        Creates a new telemetry packet.
        
        Args:
            altitude (float): Altitude in meters.
            velocity (float): Velocity in m/s.
            acc_z (float): Acceleration in Z-axis (m/s^2).
            status_code (int): Operating status code (e.g., 0=Init, 1=Flight).
        """
        self.timestamp = time.time()
        self.altitude = altitude
        self.velocity = velocity
        self.acc_z = acc_z
        self.status_code = status_code

    def pack(self) -> bytes:
        """
        Serializes the packet into a binary format suitable for RF transmission.
        
        Format: 'd f f f i' (double timestamp, float alt, float vel, float acc, int status)
        
        Returns:
            bytes: Packed binary data.
        """
        # Using 'd' for double precision timestamp, 'f' for floats, 'i' for int
        return struct.pack('dfffi', self.timestamp, self.altitude, self.velocity, self.acc_z, self.status_code)

if __name__ == "__main__":
    # Test packet creation
    packet = TelemetryPacket(altitude=150.5, velocity=-12.2, acc_z=9.81, status_code=1)
    packed_data = packet.pack()
    print(f"Telemetry Packet Size: {len(packed_data)} bytes")
    print(f"Hex Dump: {packed_data.hex()}")

