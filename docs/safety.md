# 🛡️ Vertical-Arch Mission Safety Protocols

This document outlines the safety procedures and failure mode strategies for the Dikey İnişli Roket mission.

## 1. Pre-Flight Safety Checklist
- [ ] **Battery Voltage:** Minimum 12.6V (3S LiPo).
- [ ] **Sensor Calibration:** IMU bias corrected and Baro zeroed at ground level.
- [ ] **LoRa RSSI:** Signal strength > -90dBm at 100m distance.
- [ ] **Mechanical Check:** TVC linkages secure and free from obstruction.

## 2. Failure Mode and Effects Analysis (FMEA)

| Failure Mode | Detection | Autonomous Mitigation Strategy |
| :--- | :--- | :--- |
| **IMU Divergence** | Baro vs Accel inconsistency | Switch to secondary IMU; prioritize Baro for vertical Z axis. |
| **Engine Flameout** | High negative Z-acceleration | Deployment of Emergency Parachute System. |
| **Link Loss** | Telemetri heartbeat timeout | Otonom "Safe Descent" mode; vertical stabilization focus. |
| **Thrust Saturation**| PID output > Max Thrust | Recalculate descent slope; attempt steeper glide path. |

## 3. Emergency Kill Switch (EKS)
Mandatory manual override for ground control. In case of safety perimeter breach, the ground station will send the `0xFF_SHUTDOWN` packet to terminate all propulsion immediately.

---
© 2025 Vertical-Arch Safety Board.
