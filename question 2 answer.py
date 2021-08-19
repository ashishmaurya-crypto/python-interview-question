import requests
import pprint
for page in range(13):
    url = 'https://reqres.in/api/users?page=%s'%page
    data = requests.get(url)
    pprint.pprint(data.json())