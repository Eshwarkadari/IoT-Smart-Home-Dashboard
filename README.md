# 🏠 IoT Smart Home Dashboard

> Real-time home monitoring system using **Python, MQTT, Raspberry Pi & Power BI** — the kind of project that gets you hired at IoT and embedded companies.

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Raspberry Pi](https://img.shields.io/badge/Raspberry_Pi-C51A4A?style=for-the-badge&logo=raspberry-pi&logoColor=white)
![MQTT](https://img.shields.io/badge/MQTT-3C5280?style=for-the-badge&logo=eclipse-mosquitto&logoColor=white)
![Power BI](https://img.shields.io/badge/Power_BI-F2C811?style=for-the-badge&logo=powerbi&logoColor=black)
![Arduino](https://img.shields.io/badge/Arduino-00979D?style=for-the-badge&logo=arduino&logoColor=white)

---

## 📌 Project Overview

A complete **IoT Smart Home monitoring system** that collects real-time sensor data (temperature, humidity, motion, light, gas) and visualizes it on a **Power BI live dashboard**.

This is exactly the kind of project that gets attention at:
- 🏢 **Bosch, Honeywell, Siemens** (IoT/Embedded roles)
- 💻 **TCS, Infosys, Wipro** (IoT Developer roles)
- 🚀 **Startups** building smart home products

---

## 🏗️ System Architecture

```
[Sensors] → [Arduino/Raspberry Pi] → [MQTT Broker] → [Python Subscriber]
                                                              ↓
                                                     [SQLite Database]
                                                              ↓
                                                     [Power BI Dashboard]
```

---

## ✨ Features

- 🌡️ **Temperature & Humidity** monitoring (DHT11/DHT22)
- 💡 **Light intensity** detection (LDR sensor)
- 🚶 **Motion detection** (PIR sensor)
- 🔥 **Gas/smoke alert** system (MQ-2 sensor)
- 📡 **MQTT protocol** for real-time data transmission
- 🗄️ **SQLite database** for data storage
- 📊 **Power BI dashboard** with live charts
- 🔔 **Alert system** — email/SMS when threshold exceeded
- 📱 **REST API** to access sensor data remotely

---

## 🗂️ Project Structure

```
IoT-Smart-Home-Dashboard/
├── hardware/
│   ├── circuit_diagram.md        # Wiring guide
│   └── arduino_sensor.ino        # Arduino sensor code
├── python/
│   ├── mqtt_publisher.py         # Simulate/publish sensor data
│   ├── mqtt_subscriber.py        # Receive and store data
│   ├── database.py               # SQLite operations
│   ├── api.py                    # Flask REST API
│   └── alert_system.py           # Threshold alerts
├── data/
│   └── sensor_readings.csv       # Sample sensor data
├── powerbi/
│   └── dashboard_guide.md        # Power BI setup
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### Prerequisites
```bash
pip install paho-mqtt flask pandas sqlite3
```

### Run the Simulator (without hardware)
```bash
python python/mqtt_publisher.py --simulate
python python/mqtt_subscriber.py
```

### With Real Hardware (Raspberry Pi)
```bash
# On Raspberry Pi
pip install RPi.GPIO Adafruit_DHT paho-mqtt
python python/mqtt_publisher.py --hardware
```

### Start REST API
```bash
python python/api.py
# Access at http://localhost:5000/api/sensors
```

---

## 📊 Sensor Data Format (MQTT Payload)

```json
{
  "device_id": "home_sensor_01",
  "timestamp": "2024-01-15 10:30:00",
  "temperature": 28.5,
  "humidity": 65.2,
  "motion": true,
  "light_level": 450,
  "gas_level": 120,
  "location": "Living Room"
}
```

---

## 📈 Power BI Dashboard Pages

| Page | Visuals |
|------|---------|
| Live Overview | Current temp, humidity, motion status |
| Trends | 24-hour sensor trend lines |
| Alerts | All threshold breach events |
| Room Analysis | Sensor data by room/location |

---

## 🔧 Hardware Components

| Component | Purpose | Cost (approx) |
|-----------|---------|---------------|
| Raspberry Pi 4 / Arduino Uno | Main controller | ₹2,000–₹4,000 |
| DHT22 | Temp & Humidity | ₹150 |
| PIR Sensor | Motion detection | ₹80 |
| LDR Module | Light sensing | ₹30 |
| MQ-2 Gas Sensor | Gas/smoke detection | ₹120 |

---

## 👨‍💻 Author

**Kadari Eshwar** — ECE Student, JNTU Hyderabad
[GitHub](https://github.com/Eshwarkadari) | [LinkedIn](https://www.linkedin.com/in/eshwar-kadari-134aa4278)
