import urllib.request
import json

data = json.dumps({"username": "newfarmer", "password": "password123", "email": "new@farmer.com", "first_name": "New", "last_name": "Farmer"}).encode("utf-8")
req = urllib.request.Request("http://127.0.0.1:8000/api/auth/register/", data=data, headers={"Content-Type": "application/json"})
try:
    response = urllib.request.urlopen(req)
    print("SUCCESS:")
    print(response.read().decode("utf-8"))
except urllib.error.HTTPError as e:
    print(f"Error {e.code}: {e.read().decode('utf-8')}")
except Exception as e:
    print(f"Error: {e}")
