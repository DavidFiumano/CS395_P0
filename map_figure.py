import plotly.express as px

# This is how you make a basic map.
# Generally, lat and lon refer to lists of points that you wish to display.
# Center centers the map, and zoom sets the map zoom.
chicago_map = px.scatter_mapbox(lat=[41.8781], lon=[-87.6298], center={'lat' : 41.8781, 'lon' : -87.6298}, zoom=10)
chicago_map.update_layout(mapbox_style="open-street-map") # set map style
chicago_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0}) # let map extend screen to screen

# you can do the same thing using graph_objects. See here: 
# https://plotly.com/python/scattermapbox/