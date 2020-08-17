import plotly.express as px

chicago_map = px.scatter_mapbox(lat=[41.8781], lon=[-87.6298], center={'lat' : 41.8781, 'lon' : -87.6298}, zoom=10)
chicago_map.update_layout(mapbox_style="open-street-map") # set map style
chicago_map.update_layout(margin={"r":0,"t":0,"l":0,"b":0})