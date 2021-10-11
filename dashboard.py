# Dashboard for KFM Bot

# Imports
from flask import Flask
from threading import Thread

# Create flask app
dashboard = Flask("")

# Main page
@dashboard.route("/")
def dashboard():
    # Read logs
    with open("/Core/Logs/system.kfmlog", "r") as file:
        return file.read()

# Execute
def run():
    dashboard.run(host="0.0.0.0", port=8080)

# Create thread
def deploy():
    server = Thread(target=run)
    server.start()