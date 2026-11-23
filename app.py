from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def home():
    return "Welcome! I deployed and updated this server myself."


@app.get("/health")
def health():
    return jsonify(status="ok")
