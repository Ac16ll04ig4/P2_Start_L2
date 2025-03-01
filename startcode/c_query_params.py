import requests

naam = input("Wat is je naam? ")

response = requests.get(
    url='https://api.agify.io/',
    params={'name': naam}
    )
if response.status_code == 200:
    data = response.json()
    print(data['age'])
else:
    print(f'error code{response.status_code}')

