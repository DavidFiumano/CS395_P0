import plotly
import plotly.graph_objects as go

import dash
import dash_core_components as dcc
import dash_html_components as html

from aot_api.data_fetcher import getData
from aot_api.AOTNode import AOTNode, Measurement

def createCO2Graph():
    return go.Figure()

def createNO2Graph():
    return go.Figure()

def create3umGraph():
    return go.Figure()

def create5umGraph():
    return go.Figure()