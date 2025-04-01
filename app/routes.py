from flask import render_template
from app import app
from app.metrics import collect_metrics
import time

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/metrics')
def metrics():
    # Update metrics before exposing them
    collect_metrics()
    time.sleep(1)  # Small delay to ensure metrics are collected
    return "Metrics updated"