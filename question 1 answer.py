import requests
import pprint


res = requests.get('https://my-json-server.typicode.com/typicode/demo/posts')
res2 = requests.get('https://my-json-server.typicode.com/typicode/demo/comments')
print(res.status_code)
print(res2.status_code)

pprint.pprint(res.json())

pprint.pprint(res2.json())



