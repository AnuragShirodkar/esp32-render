from flask import Flask, jsonify

app = Flask(__name__)


@app.get("/")
def home():
    return "Hello! My first Render server is running."


@app.get("/health")
def health():
    return jsonify(status="ok")
