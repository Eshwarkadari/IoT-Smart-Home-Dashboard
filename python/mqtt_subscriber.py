"""
mqtt_subscriber.py  —  Receive & Store Sensor Data
Author: Kadari Eshwar | B.Tech ECE, JNTU Hyderabad
"""

import paho.mqtt.client as mqtt
import json
from database import SensorDB

BROKER = "broker.hivemq.com"
PORT   = 1883
TOPIC  = "smarthome/sensors"

db = SensorDB()

THRESHOLDS = {
    "temperature": 35.0,
    "humidity":    80.0,
    "gas_level":   250,
}

def check_alerts(data):
    """Check if any sensor value exceeds threshold."""
    for key, limit in THRESHOLDS.items():
        if data.get(key, 0) > limit:
            print(f"  ⚠️  ALERT! {key.upper()} = {data[key]} exceeds {limit} in {data['room']}")

def on_message(client, userdata, msg):
    try:
        data = json.loads(msg.payload.decode())
        db.insert(data)
        check_alerts(data)
        print(f"💾 Stored: {data['room']} | Temp: {data['temperature']}°C | Hum: {data['humidity']}%")
    except Exception as e:
        print(f"❌ Error: {e}")

def on_connect(client, userdata, flags, rc):
    print(f"✅ Connected! Subscribing to {TOPIC}")
    client.subscribe(TOPIC)

client = mqtt.Client()
client.on_connect = on_connect
client.on_message = on_message
client.connect(BROKER, PORT, 60)

print("👂 Listening for sensor data... (Ctrl+C to stop)")
client.loop_forever()
