import requests

response = requests.get('https://httpbin.org/ip')
print('Welcome to Planet No Limits.')
print('Your IP is {0}'.format(response.json()['origin']))