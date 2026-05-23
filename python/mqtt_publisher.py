"""
mqtt_publisher.py  —  IoT Sensor Data Publisher
Simulates or reads real sensor data and publishes via MQTT
Author: Kadari Eshwar | B.Tech ECE, JNTU Hyderabad
"""

import paho.mqtt.client as mqtt
import json, time, random, argparse
from datetime import datetime

BROKER   = "broker.hivemq.com"
PORT     = 1883
TOPIC    = "smarthome/sensors"

ROOMS = ["Living Room", "Bedroom", "Kitchen", "Bathroom", "Hall"]

def simulate_sensor_data(room):
    """Simulate realistic sensor readings."""
    return {
        "device_id":   f"sensor_{room.lower().replace(' ','_')}",
        "timestamp":   datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "room":        room,
        "temperature": round(random.uniform(22.0, 35.0), 1),
        "humidity":    round(random.uniform(40.0, 80.0), 1),
        "motion":      random.choice([True, False]),
        "light_level": random.randint(100, 1000),
        "gas_level":   random.randint(50, 300),
    }

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print(f"✅ Connected to MQTT Broker: {BROKER}")
    else:
        print(f"❌ Connection failed. Code: {rc}")

def main(simulate=True):
    client = mqtt.Client()
    client.on_connect = on_connect
    client.connect(BROKER, PORT, 60)
    client.loop_start()

    print(f"📡 Publishing sensor data to topic: {TOPIC}")
    print("   Press Ctrl+C to stop\n")

    try:
        while True:
            for room in ROOMS:
                data = simulate_sensor_data(room)
                payload = json.dumps(data)
                client.publish(TOPIC, payload)
                print(f"📤 [{data['timestamp']}] {room}: "
                      f"Temp={data['temperature']}°C  "
                      f"Hum={data['humidity']}%  "
                      f"Motion={data['motion']}")
            time.sleep(5)
    except KeyboardInterrupt:
        print("\n🛑 Publisher stopped.")
        client.loop_stop()

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--simulate", action="store_true", default=True)
    parser.add_argument("--hardware", action="store_true")
    args = parser.parse_args()
    main(simulate=not args.hardware)
