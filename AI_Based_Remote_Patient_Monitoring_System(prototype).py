import numpy as np
import pandas as pd
from sklearn.ensemble import IsolationForest
import time

# 1. Simulated Health Data Generator
def generate_health_data():
    heart_rate = np.random.normal(75, 10)       # Normal resting heart rate
    blood_pressure = np.random.normal(120, 15)  # Normal systolic BP
    oxygen_level = np.random.normal(98, 2)      # Normal oxygen saturation
    return [heart_rate, blood_pressure, oxygen_level]

# 2. Historical Data for Model Training
np.random.seed(42)
historical_data = np.array([generate_health_data() for _ in range(1000)])

# 3. Anomaly Detection Model (Isolation Forest)
model = IsolationForest(contamination=0.05)
model.fit(historical_data)

# 4. Real-Time Monitoring Simulation
def monitor_patient():
    print("Starting real-time patient monitoring...")
    while True:
        current_data = np.array(generate_health_data()).reshape(1, -1)
        prediction = model.predict(current_data)  # -1 = Anomaly, 1 = Normal

        heart_rate, blood_pressure, oxygen_level = current_data[0]
        print(f"HR: {heart_rate:.1f}, BP: {blood_pressure:.1f}, O2: {oxygen_level:.1f}%")

        if prediction[0] == -1:
            print("⚠️ ALERT: Abnormal health reading detected! Notify healthcare provider.")

        time.sleep(2)  # Simulate real-time data feed every 2 seconds

# Run the monitoring system
if __name__ == "__main__":
    try:
        monitor_patient()
    except KeyboardInterrupt:
        print("\nMonitoring stopped.")
