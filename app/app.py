from flask import Flask, jsonify, render_template
from datetime import datetime, UTC
import os
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s %(levelname)s %(message)s"
)

app = Flask(__name__)


@app.route("/")
def dashboard():
    app.logger.info("Dashboard accessed")
    return render_template("index.html")


@app.route("/health")
def health():
    app.logger.info("Health endpoint called")

    return jsonify({
    "status": "UP",
    "timestamp": datetime.now(UTC).isoformat()
})


@app.route("/robots")
def robots():
    app.logger.info("Robots endpoint called")

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
        },
        {
            "robotId": "AGV-103",
            "status": "ACTIVE",
            "battery": 95,
            "location": "Zone-C"
        }
    ])


@app.route("/metrics")
def metrics():
    app.logger.info("Metrics endpoint called")

    return jsonify({
        "active_robots": 2,
        "charging_robots": 1,
        "healthy_robots": 3
    })


@app.route("/version")
def version():
    app.logger.info("Version endpoint called")

    return jsonify({
        "application": "Robotics Fleet Management Platform",
        "version": "1.0.0",
        "environment": os.getenv("ENVIRONMENT", "production")
    })


@app.route("/monitor")
def monitor():

    app.logger.info("Monitor endpoint called")

    return jsonify({
        "application_status": "UP",
        "active_robots": 2,
        "charging_robots": 1,
        "healthy_robots": 3,
        "container_runtime": "Docker",
        "deployment_strategy": "Rolling Update",
        "environment": "Production"
    })


@app.route("/info")
def info():
    app.logger.info("Info endpoint called")

    return jsonify({
        "project": "Robotics Fleet Management Platform",
        "ci_cd": "GitHub Actions",
        "container_runtime": "Docker",
        "orchestration": "Kubernetes",
        "monitoring": "Prometheus",
        "deployment_strategy": "Rolling Update"
    })


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)