import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd
import json

app = dash.Dash()

df = pd.read_csv('../../notebooks/Data/wheels.csv')
