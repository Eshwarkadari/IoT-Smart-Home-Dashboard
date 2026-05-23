"""
database.py  —  SQLite Database for Sensor Readings
Author: Kadari Eshwar | B.Tech ECE, JNTU Hyderabad
"""

import sqlite3, pandas as pd
from datetime import datetime

class SensorDB:
    def __init__(self, db_path="sensor_data.db"):
        self.db_path = db_path
        self._init_db()

    def _init_db(self):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                CREATE TABLE IF NOT EXISTS sensor_readings (
                    id          INTEGER PRIMARY KEY AUTOINCREMENT,
                    device_id   TEXT,
                    timestamp   TEXT,
                    room        TEXT,
                    temperature REAL,
                    humidity    REAL,
                    motion      INTEGER,
                    light_level INTEGER,
                    gas_level   INTEGER
                )
            """)

    def insert(self, data):
        with sqlite3.connect(self.db_path) as conn:
            conn.execute("""
                INSERT INTO sensor_readings
                (device_id, timestamp, room, temperature, humidity, motion, light_level, gas_level)
                VALUES (?,?,?,?,?,?,?,?)
            """, (
                data.get("device_id"), data.get("timestamp"), data.get("room"),
                data.get("temperature"), data.get("humidity"),
                1 if data.get("motion") else 0,
                data.get("light_level"), data.get("gas_level")
            ))

    def get_all(self):
        with sqlite3.connect(self.db_path) as conn:
            return pd.read_sql("SELECT * FROM sensor_readings ORDER BY timestamp DESC", conn)

    def export_csv(self, path="sensor_readings.csv"):
        df = self.get_all()
        df.to_csv(path, index=False)
        print(f"✅ Exported {len(df)} rows to {path}")
        return path
