import random
import datetime
import os
import time

SERVICES = ["sqldb", "ui", "frontend.js", "frontend.flask", "backend.flask"]
log_levels = ["INFO", "WARNING", "ERROR", "CRITICAL"]
level_weights = [0.6, 0.25, 0.1, 0.05]

messages = {
    "INFO": ["this is", "some real", "big info", "on this code"],
    "WARNING": ["wow look", "at this !!", "big sign", "huge warning"],
    "ERROR": ["you got", "an error", "because you", "really suck"],
    "CRITICAL": ["dude this", "is a very", "scary critical", "huge mistake"]
}

def get_timestamp():
    now = datetime.datetime.now()
    return now.strftime("%Y-%m-%d %H:%M:%S,%f")[:-3]
if not os.path.exists("logs"):
    os.makedirs("logs")
for service in SERVICES:
    filename = f"logs/{service}.log"
    entries = random.random.randint(50, 100)
    with open(filename, "w") as f:
        for _ in range(entries):
            level = random.choices(log_levels, weights=level_weights)[0]
            if service in ["sqldb", "backend.js"] and random.random() < 0.3:
                level = random.choice(["ERROR", "CRITICAL"])
            message = random.choice(messages[level])
            timestamp = get_timestamp()
            f.write(f"{timestamp} | {service} | {level} | {message}\n")
print("log files created in logs directory")