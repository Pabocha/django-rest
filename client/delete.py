import requests
from getpass import getpass
endpoint = "http://localhost:8000/api/api-token-auth/"
username = input("veuillez saisir votre nom d'utilisateur \n")
password = getpass("veuillez saisir votre mot de passe \n")
auth_response = requests.post(endpoint, json={'username':username, 'password':password})
print (auth_response.json())
token = auth_response.json().get('token')


if auth_response.status_code == 200:
    endpoint = "http://localhost:8000/product/create/"
    response = requests.post(endpoint, json={'name': 'franbroise', 'content': 'essaye pour savourer le goût du desire', 'price':2.55})
    headers = {
        'Authorization': f'Token {token}'
    }
    id=input("veuillez saisir un id à supprimer ")
    endpoint = f"http://localhost:8000/product/{id}/delete/"
    response = requests.delete(endpoint, headers=headers)
    print(response.status_code, response.status_code==204)
