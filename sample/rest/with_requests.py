import requests

params = {'key1': 'value1', 'key2': 'value2'}

# GET method
response = requests.get('http://httpbin.org/get', params=params, timeout=1)
print(response.status_code)
print(response.text)
print(response.json())

# POST method
response = requests.post('http://httpbin.org/post', data=params, timeout=1)
print(response.status_code)
print(response.text)
print(response.json())
