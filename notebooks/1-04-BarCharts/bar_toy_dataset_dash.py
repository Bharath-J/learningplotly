import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go

app = dash.Dash()

df = pd.read_csv('../../notebooks/Data/mocksurvey.csv')
df['target'] = data['target']
print(df.head())
