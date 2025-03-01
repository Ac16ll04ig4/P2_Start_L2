import requests

request = requests.get('https://official-joke-api.appspot.com/random_joke')
if request.status_code == 200:
    print(request.text)
else:
    print('Er is iets misgelopen, foutcode'{request.status_code})
