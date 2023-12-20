import requests
id = input("veuillez le id à supprimer ")

endpoint = f"http://localhost:8000/product/{id}/update/"
response = requests.patch(endpoint, json={'name':'citronelle', 'content':'feuilles pour du lait'})
print(response.json())
print(response.status_code)
