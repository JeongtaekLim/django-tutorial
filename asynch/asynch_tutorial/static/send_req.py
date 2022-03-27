import requests

status = requests.get('http://192.168.0.5:8000/ajax/echo')
print(status)