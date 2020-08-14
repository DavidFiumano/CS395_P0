import requests
from pprint import PrettyPrinter
import geojson
import json
from datetime import datetime
from AOTNode import AOTNode, Measurement

# get a list of AOT Nodes and return it as a list
def getAOTNodes(project : str = None, size : int = 200):
    if project != None:
        req_str = 'https://api.arrayofthings.org/api/nodes?size=' + str(size) + "&project=" + project
    else:
        req_str = 'https://api.arrayofthings.org/api/nodes?size=' + str(size)

    response = requests.get(req_str)
    
    nodes = response.json()['data']
    node_list = list()

    for node in nodes:
        vsn = node['vsn']
        location = geojson.loads(json.dumps(node['location']))
        description = node['description']
        address = node['address']

        node_obj = AOTNode(vsn=vsn, location=location, address=address, description=description)

        node_list.append(node_obj)

    return node_list

def updateMeasurements(nodes : list, size : int):
    
    # TODO this could be more efficient in terms of calls to the api. We could instead construct the list of nodes and match them to the right data later
    for node in nodes:
        req_str = 'https://api.arrayofthings.org/api/observations?node[]=' + str(node.vsn) +'&size=' + str(size)
        response = requests.get(req_str)
        
        observations = response.json()['data']
        if len(observations) == 0:
            continue

        for observation in observations:
            
            uom = observation['uom']

            ts = observation['timestamp']
            date, time = ts.split('T')
            year, month, day = date.split('-')
            hour, minute, second = time.split(':')

            timestamp = datetime(int(year), int(month), int(day), int(hour), int(minute), int(second))

            value = observation['value']

            measurement = Measurement(uom, timestamp, value)

            sensorpath = observation['sensor_path']

            node.updateMeasurement(sensorpath, measurement)

# returns a list of nodes without empty measurements
def stripEmptyNodes(nodes : list):
    ret_list = list()
    for node in nodes:
        if len(node.getMeasurements()) == 0:
            continue
        ret_list.append(node)

    return ret_list

ns = getAOTNodes(project="chicago", size=200)

#for n in ns:
#    print(n)

updateMeasurements(ns, 200)

#for n in ns:
#    print(n)

ns = stripEmptyNodes(ns)
print(len(ns))
for n in ns:
    print(n)
    measurements = n.getMeasurements()
    for measurement in measurements:
        print(str(measurement))

    print()
    print()