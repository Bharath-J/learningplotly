import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from sklearn import datasets

app = dash.Dash()

data = datasets.load_boston()
