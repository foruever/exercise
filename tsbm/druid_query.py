import requests
import json

url = 'http://127.0.0.1:8082/druid/v2?pretty'
headers={
    "Content-Type":"application/json"
}
dat=json.dumps({"filter":{"type":"and","fields":[{"type":"selector","dimension":"device_code","value":"d_42"},{"type":"selector","dimension":"sensor_code","value":"s_2"}]},"intervals":["2018-01-03T04:54:33.277/2018-01-03T05:54:33.277"],"granularity":"all","pagingSpec":{"threshold":5,"pagingIdentifiers":{}},"metrics":[],"dataSource":"druidTest","queryType":"select","dimensions":[]})
r = requests.post(url, headers=headers,data=dat)
print(r.text)