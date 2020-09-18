import dash
import dash_html_components as html
import dash_core_components as dcc
from dash.dependencies import Input,Output
import requests

app = dash.Dash()

app.layout = html.Div([
            html.Div([
                    html.Iframe(src="https://www.flightradar24.com",
                    height=500,width=1200)
            ])
            html.Div([
            html.Pre(id='counter_text',
            children='Active Flights Worldwide'),
            dcc.Interval(id='interval-component',
            interval=6000,
            n_intervals=0)
            ])
])

#def update_layout(n):
