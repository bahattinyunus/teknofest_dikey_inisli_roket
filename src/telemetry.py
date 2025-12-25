import struct
import time

class TelemetryPacket:
    """
    Defines the data structure for rocket-to-ground communication.
    """
    def __init__(self, altitude, velocity, acc_z, status_code):
        self.timestamp = time.time()
        self.altitude = altitude
        self.velocity = velocity
        self.acc_z = acc_z
        self.status_code = status_code

    def pack(self):
        # Example binary packing for LoRa transmission
        return struct.pack('ffffi', self.timestamp, self.altitude, self.velocity, self.acc_z, self.status_code)

if __name__ == "__main__":
    packet = TelemetryPacket(altitude=150.5, velocity=-12.2, acc_z=9.81, status_code=1)
    print(f"Data Packet Created: {len(packet.pack())} bytes")
