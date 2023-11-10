import requests

endpoint = "http://localhost:8000/api/products/"
data = {
    "title": "test123",
    "price": 32.00
}

get_response = requests.post(endpoint, json = data)

print(get_response.json())