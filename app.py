from flask import Flask, jsonify, render_template

app = Flask(__name__)


@app.get("/")
def home():
    return render_template("index.html")


@app.get("/health")
def health():
    return jsonify(status="ok")
@app.get("/api/status")
def device_status():
    return jsonify(
        device="ESP32",
        connected=False,
        led="UNKNOWN",
        message="Waiting for ESP32 connection"
    )
