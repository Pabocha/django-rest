import requests
id=input("veuillez saisir un id à rechercher ")
endpoint = f"http://localhost:8000/product/{id}/detail/"
response = requests.get(endpoint)
print(response.json())
print(response.status_code)
