import requests

response = requests.post('http://localhost:5000/predict', files={'image': open('../fructe.jpg', 'rb')})

a = response.json()
x=1
