"""
api.py  —  Flask REST API for Sensor Data
Author: Kadari Eshwar | B.Tech ECE, JNTU Hyderabad
"""

from flask import Flask, jsonify, request
from database import SensorDB

app = Flask(__name__)
db  = SensorDB()

@app.route("/api/sensors", methods=["GET"])
def get_all():
    """Get all sensor readings."""
    df = db.get_all()
    return jsonify(df.to_dict(orient="records"))

@app.route("/api/sensors/latest", methods=["GET"])
def get_latest():
    """Get latest reading per room."""
    df = db.get_all()
    latest = df.groupby("room").first().reset_index()
    return jsonify(latest.to_dict(orient="records"))

@app.route("/api/sensors/room/<room_name>", methods=["GET"])
def get_by_room(room_name):
    """Get readings for a specific room."""
    df = db.get_all()
    room_data = df[df["room"].str.lower() == room_name.lower()]
    return jsonify(room_data.to_dict(orient="records"))

@app.route("/api/sensors/alerts", methods=["GET"])
def get_alerts():
    """Get all readings that exceeded thresholds."""
    df = db.get_all()
    alerts = df[(df["temperature"] > 35) | (df["humidity"] > 80) | (df["gas_level"] > 250)]
    return jsonify(alerts.to_dict(orient="records"))

if __name__ == "__main__":
    print("🚀 API running at http://localhost:5000")
    app.run(debug=True, port=5000)
