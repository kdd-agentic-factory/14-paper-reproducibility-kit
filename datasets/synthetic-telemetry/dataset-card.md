# Dataset Card — Synthetic Telemetry v1

## Dataset ID

synthetic-telemetry-v1

## Description

Synthetic motorcycle telemetry dataset generated for reproducibility and
demonstration of the KDD-governed race engineering architecture. Simulates
two free practice sessions (FP1, FP2) with 5,000 samples each at 100 Hz
effective sampling rate.

## Classification

Public synthetic.

## Contents

Each row contains:

| Column | Description | Unit |
|--------|-------------|------|
| ts_micro | Timestamp | microseconds |
| gps_lat | GPS latitude (synthetic) | degrees |
| gps_lon | GPS longitude (synthetic) | degrees |
| imu_yaw | Yaw angle | degrees |
| imu_pitch | Pitch angle | degrees |
| imu_roll | Roll/lean angle | degrees |
| tps | Throttle position sensor | % |
| brake_press_front | Front brake pressure | bar |
| brake_press_rear | Rear brake pressure | bar |
| susp_travel_f | Front suspension travel | mm |
| susp_travel_r | Rear suspension travel | mm |
| tire_temp_surface | Tyre surface temperature | °C |
| tire_temp_carcass | Tyre carcass temperature | °C |
| wheel_speed_f | Front wheel speed | km/h |
| wheel_speed_r | Rear wheel speed | km/h |
| gps_speed | GPS-derived speed | km/h |
| rpm | Engine RPM | rpm |
| gear | Gear position | 1–6 |
| tcs_level | Traction control intervention level | 0–10 |
| engine_map | Engine mapping name | string |

## Generation Method

Generated using `scripts/generate-synthetic-telemetry.py` with NumPy random
number generator, seed 42. Signals are constructed from sinusoidal patterns
plus Gaussian noise to approximate realistic telemetry structure.

## Sensitive Data

No real rider, team, bike, or circuit telemetry is included. GPS coordinates
are synthetic and do not correspond to any real circuit.

## Intended Use

- feature extraction validation,
- tyre degradation pattern detection,
- reproducibility demonstration,
- paper artifact validation.

## Limitations

Synthetic data does not fully represent real MotoGP telemetry complexity.
Missing: aerodynamic channels, detailed engine maps, fuel consumption, real
GPS trajectories, tyre compound identity.
