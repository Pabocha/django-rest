import requests

endpoint = "http://localhost:8000/product/"
response = requests.post(endpoint, json={'name':'mangue', 'content':'toast the good fruit', 'price':19.99})
print(response.json())
print(response.status_code)
