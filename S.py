import requests
import os
import time


for j in range(20):
    print(j)
    for i in range(50):
        requests.get("http://localhost:8000/")
        requests.get("http://localhost:8000/foo")
    time.sleep(10)

time.sleep(2*60)