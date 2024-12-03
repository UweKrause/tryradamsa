import requests
import time

SERVER_URL = "http://server:5000"

while True:
    try:
        data = {"message": "Hello from the client!"}
        response = requests.post(SERVER_URL, json=data)
        print(f"Server responded with: {response.json()}")
    except Exception as e:
        print(f"Error: {e}")
    time.sleep(5)  # Wait for 5 seconds before sending the next request