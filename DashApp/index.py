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
                dcc.Interval(id='graph_update_interval', interval=300000), # update graphs every 5 min, when new data is ready
                html.H1("CS 395 Project 0"),
                dcc.Dropdown(id='graph_selector', options=dropdown_opts, value='CO2_Graph'),
                html.Button('Take an Interactive Snapshot', id='graph_snapshot_button', n_clicks=0),
                html.H3(id='snapshot_text'),
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
    if value == None:
        return createCO2Graph()
    elif value == 'CO2_Graph':
        return createCO2Graph()
    elif value == 'NO2_Graph':
        return createNO2Graph()
    elif value == '3um_Graph':
        return create3umGraph()
    elif value == '5um_Graph':
        return create5umGraph()
    else:
        print('For some reason, the graph selector was set to an unknown value: ' + str(value) + '\nDefaulting to CO2 graph.')
        return createCO2Graph()

@app.callback(
    Output('snapshot_text', 'children'),
    [
        Input('graph_snapshot_button', 'n_clicks')
    ],
    [
        State('student_graph', 'figure')
    ]
)
def take_graph_snapshot(n_clicks, figure):
    if n_clicks == None or n_clicks == 0:
        return 'No Snapshots Taken Yet...'
    else:
        fig = go.Figure(figure)
        snapshot_file = 'student_snapshot_' + str(n_clicks) + '.html'
        fig.write_html(snapshot_file, include_plotlyjs='cdn')
        return 'Most Recent Snapshot Saved in ' + snapshot_file