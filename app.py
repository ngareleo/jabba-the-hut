from flask import Flask
"""
Application
main entry point => app.py
The system has 2 services running
1. Asset tracking service
2. Http server
"""

app = Flask(__name__)


@app.route('/')
def index():
    return "Welcome Runner"

