import requests
url ="http://127.0.0.1:5000/api/chat"
payload = {
    "question": "What is daniyal doing ?",
    "context": "Daniyal is a student and building his first project."
}
try:
    response = requests.post(url, json=payload)
    print("Response:", response.json())
    print("status code:", response.status_code)
except Exception as e:
    print(f"An error occurred: {e}")