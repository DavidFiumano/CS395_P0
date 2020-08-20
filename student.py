import plotly
import plotly.graph_objects as go
import plotly.express as px

import dash
import dash_core_components as dcc
import dash_html_components as html

from aot_api.data_fetcher import getData
from aot_api.AOTNode import AOTNode, Measurement
from map_figure import chicago_map

def createWeatherGraph():   
    return chicago_map

def createGasGraph():
    return chicago_map

def createParticulateGraph():
    return chicago_map