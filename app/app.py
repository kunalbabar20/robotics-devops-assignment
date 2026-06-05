from flask import Flask, jsonify, render_template
from datetime import datetime
import os

app = Flask(__name__)

@app.route("/")
def dashboard():
    return render_template("index.html")

@app.route("/health")
def health():
    return jsonify({
        "status": "UP",
        "timestamp": datetime.utcnow().isoformat()
    })

@app.route("/robots")
def robots():
    return jsonify([
        {
            "robotId": "AGV-101",
            "status": "ACTIVE",
            "battery": 82,
            "location": "Zone-A"
        },
        {
            "robotId": "AGV-102",
            "status": "CHARGING",
            "battery": 35,
            "location": "Charging Station"
        }
    ])

@app.route("/metrics")
def metrics():
    return jsonify({
        "active_robots": 1,
        "charging_robots": 1,
        "healthy_robots": 2
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)