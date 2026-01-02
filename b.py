import time
import random
import requests
from datetime import datetime

URL = "https://skyvyr.onrender.com"

MIN_INTERVAL = 5 * 60     # 5 minutes
MAX_INTERVAL = 15 * 60    # 15 minutes

while True:
    try:
        response = requests.get(URL, timeout=10)
        print(f"[{datetime.now()}] Visited {URL} | Status: {response.status_code}")
    except Exception as e:
        print(f"[{datetime.now()}] Error: {e}")

    sleep_time = random.randint(MIN_INTERVAL, MAX_INTERVAL)
    print(f"Sleeping for {sleep_time // 60} minutes\n")
    time.sleep(sleep_time)
