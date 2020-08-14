# the purpose of this file is to serve as the "home page" for the app.
# There is a drop-down menu which allows users to select the graph 
# Each graph's callback functions are defined in the student files

import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output, State

import plotly.graph_objects as go

from .app import app

import os, sys

STUDENT_CODE_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

if STUDENT_CODE_PATH not in sys.path:
    sys.path.append(STUDENT_CODE_PATH)

from student import createCO2Graph, createNO2Graph, create3umGraph, create5umGraph

dropdown_opts = [
    {
        'label' : 'CO2 Sensors',
        'value' : 'CO2_Graph'
    },
    {
        'label' : 'NO2 Sensors',
        'value' : 'NO2_Graph'
    },
    {
        'label' : '3um Particle Sensors',
        'value' : '3um_Graph'
    },
    {
        'label' : '5um Particle Sensors',
        'value' : '5um_Graph'
    }
]

app.layout = html.Div(
    children=[
                html.H1("CS 395 Project 0"),
                dcc.Dropdown(id='graph_selector', options=dropdown_opts),
                dcc.Graph(id='student_graph')
            ]
)
        

@app.callback(
    Output('student_graph', 'figure'),
    [
        Input('graph_selector', 'value')
    ]
)
def create_app_callback(value):
    print(value)
    return go.Figure()

