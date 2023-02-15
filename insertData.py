import requests
import json
URL="http://localhost:8000/insert_data/"
data={
    'name':'mitul',
    'roll':29,
    'city':'badowala'
}

json_data=json.dumps(data)

res=requests.post(url=URL,data=json_data)
data=res.json()
print(data)
