import plotly
import plotly.graph_objects as go
import plotly.express as px

import dash
import dash_core_components as dcc
import dash_html_components as html

from aot_api.data_fetcher import getData
from aot_api.AOTNode import AOTNode, Measurement
from map_figure import chicago_map

import numpy as np

def allNodesGraph():
    data = getData() # get the data. Returns a list of AOTNode objects.

    lats = list() # make lists for the data you want to extract. 
    lons = list() # You always want to extra lat/lon data from AOTNodes so you know where to plot them on the map
    vsns = list() # You can, but are not required to, extract the node ID numbers from the nodes
    sizes = list() # to set the sizes of each node's map marker differently, store the sizes in an array
    sensors_reporting = list() # technically redundant in this case, but keep track of the number of sensors reporting for each node
    addresses = list() # a list of street addresses for the nodes
    descriptions = list() # a list of descriptions for the nodes
    # I know that sizes and sensors_reporting will be equal, this is just so I can show you how to put in custom data
    
    # get the data you want into lists to be graphed
    for node in data: # in this case, we don't really do any processing but you may want to calculate values here too.
        lats.append(node.latitude) # latitude and longitude, so you know where to plot stuff
        lons.append(node.longitude)
        
        sizes.append(len(node.getMeasurements())) # node.getMeasurements() returns a dictionary with all the measurements that node has taken.
        
        sensors_reporting.append(len(node.getMeasurements())) # The number of sensors reporting on each node
        vsns.append(node.vsn) # vsns, so we can give the name of each node
        addresses.append(node.address) # The address of the node
        descriptions.append(node.description) # The description of the node

    cm = go.Figure( # create a plotly figure to return
        go.Scattermapbox( # This figure is a type called a Scattermapbox plot
            name="All Node Map", # This is optional but can help with debugging - give the graph a name
            mode="markers", # display markers and no lines
            lat=lats, # specify latitude
            lon=lons, # specify longitude
            marker = {'size': sizes}, # specify the size of the markers. You can also specify color and other neat things this way
            customdata = np.stack([vsns, sensors_reporting, addresses, descriptions], axis=-1), # we want to add some custom data for each node, np.stack([data], axis=-1) puts it in an easy to parse format for the hovertext
            hovertemplate = 'Node %{customdata[0]} Data:<br>' + # When you hover on a node, display "Node {the vsn of the node} Data:\n"
            '| Latitude %{lat}<br>' + # | Latitude: {Node Latitude}\n
            '| Longitude %{lon}<br>' + # | Longitude: {Node Longitude}\n
            '| Sensors Reporting: %{customdata[1]}<br>' + # | Sensors Reporting: {The number of sensors reporting on this node}. Equivalent to 'Sensors Reporting: %{marker.size}'
            '| Address: %{customdata[2]}<br>' +
            '| Description: %{customdata[3]}'
        )
    )

    cm.update_layout(
        mapbox_style="open-street-map", # this is absolutely required - open-street-map is easy to use, the other styles require an api key and have annoying limitations 
        margin={"r":0,"t":0,"l":0,"b":0}, # This is optional, but specifies the margins of the map in the page
        mapbox= # If you do not include this (centering and zooming on your map), you will lose points. Please include it so we don't have to zoom in a ton to grade your stuff
            {
                "center" : go.layout.mapbox.Center(
                    lat=41.8781, # this is chicago's GPS coordinates according to google maps
                    lon=-87.6298
                ),
                "zoom" : 9 # set this to something reasonable for you and your computer. 
                # As long as we can see all the nodes and don't need to move or zoom into the graph too much to find them all, I am happy with whatever you set the 'zoom' value to
            }
    )

    return cm

def createWeatherGraph():
    return chicago_map

def createGasGraph():
    return chicago_map

def createParticulateGraph():
    return chicago_map