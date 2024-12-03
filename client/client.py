import time

import pyradamsa
import requests

SERVER_URL = "http://server:80"

data_base = b"name=examplename&password=trustno1"

radamsa = pyradamsa.Radamsa()

while True:
    try:
        data_fuzz = radamsa.fuzz(data_base)
        response = requests.post(SERVER_URL, data=data_fuzz)
        print(f"Client sends: {response.request.body}")
        print(f"Server responded with: {response.text}")
        # ToDo: Compare sent with received data

    except Exception as e:
        # ToDo: Log which input caused what error (if any)
        print(f"Error: {e}")

    time.sleep(1)
