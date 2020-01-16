import json
import urllib.parse
import urllib.request

params = {'key1': 'value1', 'key2': 'value2'}

# GET method
url = 'http://httpbin.org/get?' + urllib.parse.urlencode(params)
req = urllib.request.Request(url)

with urllib.request.urlopen(req) as res:
    body = json.loads(res.read().decode('utf-8'))
    print(body)

# POST method
data = json.dumps(params).encode('utf-8')
req = urllib.request.Request('http://httpbin.org/post', data=data, method='POST')

with urllib.request.urlopen(req) as res:
    body = json.loads(res.read().decode('utf-8'))
    print(body)
