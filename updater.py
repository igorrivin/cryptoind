import datetime
import threading 
from cryptoindex import update_weights


# Global variable to track when the weights were last updated
last_update = None

def update_weights1(**kwargs):
    update_weights(**kwargs)
    # Your logic to update weights goes here
    print("Weights updated.")
    global last_update
    last_update = datetime.datetime.now()

def should_update_weights():
    global last_update
    current_time = datetime.datetime.now()
    
    # Check if the current time is within the first 10 seconds after midnight
    # and the last update wasn't today
    if current_time.time() < datetime.time(0, 2, 0) and (last_update is None or current_time.date() > last_update.date()):
        return True
    return False

