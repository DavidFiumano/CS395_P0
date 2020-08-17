import plotly
import plotly.graph_objects as go

import dash
import dash_core_components as dcc
import dash_html_components as html

from aot_api.data_fetcher import getData
from aot_api.AOTNode import AOTNode, Measurement
from map_figure import chicago_map

def createCO2Graph():
    return chicago_map

def createNO2Graph():
    return chicago_map

def create3umGraph():
    return chicago_map

def create5umGraph():
    return chicago_map