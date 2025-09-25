#!/usr/bin/env python3
"""
Demo Flask App with Secrets Loaded from .env
This app is for testing secret scanning and DevSecOps practices.
"""

import os
from flask import Flask, jsonify
from datetime import datetime
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

app = Flask(__name__)

# -----------------------------
# Load secrets from environment
# -----------------------------
SECRETS = {
    "DB_PASS": os.getenv("DB_PASSWORD", ""),
    "AWS_KEY": os.getenv("AWS_ACCESS_KEY_ID", ""),
    "AWS_SECRET": os.getenv("AWS_SECRET_ACCESS_KEY", ""),
    "API_KEY": os.getenv("API_KEY", ""),
    "JWT_SECRET": os.getenv("JWT_SECRET", ""),
    "STRIPE_KEY": os.getenv("STRIPE_SECRET_KEY", ""),
    "GITHUB_TOKEN": os.getenv("GITHUB_TOKEN", ""),
    "REDIS_PASS": os.getenv("REDIS_PASSWORD", "")
}

# -----------------------------
# Database config
# -----------------------------
DATABASE = {
    "HOST": os.getenv("DB_HOST", "localhost"),
    "PORT": int(os.getenv("DB_PORT", 5432)),
    "NAME": os.getenv("DB_NAME", "demoapp"),
    "USER": os.getenv("DB_USER", "admin"),
    "PASSWORD": SECRETS["DB_PASS"]
}

# -----------------------------
# Flask routes
# -----------------------------
@app.route("/")
def index():
    return jsonify({
        "message": "Hello from the DevSecOps Demo App",
        "status": "active",
        "server_time": datetime.utcnow().isoformat()
    })

@app.route("/health")
def health():
    return jsonify({"status": "healthy"})

@app.route("/users")
def users():
    """Simulated user list"""
    return jsonify({
        "users": [
            {"id": 101, "name": "Alice", "email": "alice@example.com"},
            {"id": 102, "name": "Bob", "email": "bob@example.com"}
        ]
    })

@app.route("/config")
def config():
    """Expose non-sensitive configuration only"""
    return jsonify({
        "database": {
            "host": DATABASE["HOST"],
            "port": DATABASE["PORT"],
            "name": DATABASE["NAME"]
        },
        "aws_region": os.getenv("AWS_REGION", "us-west-2"),
        "api_version": os.getenv("API_VERSION", "v2")
    })

# -----------------------------
# Main
# -----------------------------
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
