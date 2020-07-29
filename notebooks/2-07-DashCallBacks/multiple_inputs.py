import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../../notebooks/Data/gapminderDataFiveYear.csv')

app = dash.Dash()
# ['mpg', 'hp', 'displacement']
features = df.columns

app.layout = html.Div([
            html.Div([
                dcc.Dropdown(id='xaxis',
                            options=[{'label':i, 'value':i} for i in features],
                            value='displacement')
            ],style={'width':'48%', 'display':'inline-block'}),
            html.Div([
                dcc.Dropdown(id='yaxis',
                            options=[{'label':i, 'value':i} for i in features],
                            value='mpg')
            )],style={'width':'48%', 'display':'inline-block'}),
            dcc.Graph(id='feature-graphic')
], style={'padding':10})
