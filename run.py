"""
IoT Smart Home Dashboard — Live Simulation
Author: Kadari Eshwar | B.Tech ECE, JNTU Hyderabad
Run: python run.py
"""
from flask import Flask, jsonify, render_template_string
import random, threading, time
from datetime import datetime
from collections import deque

app = Flask(__name__)
ROOMS = ["Living Room","Kitchen","Bedroom","Hall","Bathroom"]
history = {r: deque(maxlen=20) for r in ROOMS}

def simulate():
    while True:
        for room in ROOMS:
            history[room].append({
                "timestamp":   datetime.now().strftime("%H:%M:%S"),
                "room":        room,
                "temperature": round(random.uniform(22, 36), 1),
                "humidity":    round(random.uniform(45, 80), 1),
                "motion":      random.choice([True, False]),
                "light":       random.randint(100, 900),
                "gas":         random.randint(50, 280),
            })
        time.sleep(3)

@app.route("/")
def home(): return render_template_string(HTML)

@app.route("/api/live")
def live():
    return jsonify({r: list(history[r])[-1] for r in ROOMS if history[r]})

HTML = """<!DOCTYPE html>
<html><head>
<meta charset="UTF-8"><meta http-equiv="refresh" content="4">
<title>IoT Smart Home Dashboard</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{font-family:'Segoe UI',sans-serif;background:#0f172a;color:#e2e8f0}
nav{background:#1e293b;padding:16px 28px;display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid #334155}
.logo{font-size:18px;font-weight:700;color:#4ade80}
.live{background:#4ade8022;color:#4ade80;border:1px solid #4ade80;padding:4px 12px;border-radius:20px;font-size:12px}
.main{padding:24px 28px;max-width:1200px;margin:0 auto}
h2{margin-bottom:18px;font-size:20px}
.grid{display:grid;grid-template-columns:repeat(auto-fill,minmax(210px,1fr));gap:14px}
.card{background:#1e293b;border-radius:12px;padding:18px;border:1px solid #334155}
.room{font-size:12px;color:#94a3b8;margin-bottom:8px;text-transform:uppercase;font-weight:600}
.temp{font-size:30px;font-weight:700;color:#f472b6}
.row{display:flex;justify-content:space-between;margin-top:8px;font-size:13px;color:#94a3b8}
.val{color:#e2e8f0;font-weight:600}
.on{color:#4ade80!important}.off{color:#ef4444!important}
.alert{background:#7f1d1d;border:1px solid #ef4444;border-radius:8px;padding:10px 16px;margin-bottom:12px;font-size:13px;color:#fca5a5}
footer{text-align:center;padding:16px;color:#475569;font-size:12px;margin-top:16px}
</style></head>
<body>
<nav>
  <div class="logo">🏠 IoT Smart Home Dashboard</div>
  <div class="live">● LIVE — auto refresh 4s</div>
</nav>
<div class="main">
  <h2>🌡️ Real-time Sensor Readings</h2>
  <div id="alerts"></div>
  <div class="grid" id="cards">Loading...</div>
  <p style="color:#64748b;font-size:13px;margin-top:14px">
    Built by <b style="color:#94a3b8">Kadari Eshwar</b> — B.Tech ECE, JNTU Hyderabad
  </p>
</div>
<footer>Simulating: Temperature · Humidity · Motion · Light · Gas sensors</footer>
<script>
fetch('/api/live').then(r=>r.json()).then(data=>{
  const alerts=[];
  const cards=Object.values(data).map(s=>{
    if(s.temperature>34) alerts.push('⚠️ High temperature in '+s.room+': '+s.temperature+'°C');
    if(s.gas>250) alerts.push('🚨 High gas level in '+s.room+': '+s.gas+' ppm');
    return '<div class="card"><div class="room">'+s.room+'</div><div class="temp">'+s.temperature+'°C</div>'
      +'<div class="row"><span>Humidity</span><span class="val">'+s.humidity+'%</span></div>'
      +'<div class="row"><span>Motion</span><span class="val '+(s.motion?'on':'off')+'">'+(s.motion?'Detected':'None')+'</span></div>'
      +'<div class="row"><span>Light</span><span class="val">'+s.light+' lux</span></div>'
      +'<div class="row"><span>Gas</span><span class="val">'+s.gas+' ppm</span></div>'
      +'<div class="row"><span>Updated</span><span class="val">'+s.timestamp+'</span></div></div>';
  }).join('');
  document.getElementById('cards').innerHTML=cards||'Loading...';
  document.getElementById('alerts').innerHTML=alerts.map(a=>'<div class="alert">'+a+'</div>').join('');
});
</script></body></html>"""

if __name__ == "__main__":
    threading.Thread(target=simulate, daemon=True).start()
    print("\n✅ Sensor simulation started!")
    print("🌐 Open http://localhost:5000 in your browser")
    print("   Auto-refreshes every 4 seconds")
    print("   Press Ctrl+C to stop\n")
    app.run(host="0.0.0.0", port=5000, debug=False)
