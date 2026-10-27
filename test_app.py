import requests

url = "http://127.0.0.1:5000/api/chat"
payload = {
    "question": "What program is Daniyal studying?",
    "context": "Daniyal is an IT student pursuing his Bachelor of Science in Information Technology at Mushtaq Ahmad Gurmani Science College."
}

try:
    response = requests.post(url, json=payload)
    print("Status Code:", response.status_code)
    print("Response JSON:", response.json())
except Exception as e:
    print("Error connecting to API:", e)