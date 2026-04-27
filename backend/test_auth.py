import urllib.request
import json

data = json.dumps({"username": "farmer", "password": "password123"}).encode("utf-8")
req = urllib.request.Request("http://127.0.0.1:8000/api/auth/login/", data=data, headers={"Content-Type": "application/json"})
try:
    response = urllib.request.urlopen(req)
    print(response.read().decode("utf-8"))
except Exception as e:
    print(f"Error: {e}")
