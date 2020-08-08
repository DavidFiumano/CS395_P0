import requests
from pprint import PrettyPrinter
import geojson 

point = geojson.Point((41.8781, -87.6298))
print(type(point))

pp = PrettyPrinter()

response = requests.get('https://api.arrayofthings.org/api/nodes?size=1&project=chicago')
vsn = response.json()['data'][0]['vsn']
pp.pprint(response.json())
print(vsn)
response = requests.get('https://api.arrayofthings.org/api/observations?size=100&node[]='+str(vsn))
pp.pprint(response.json())
