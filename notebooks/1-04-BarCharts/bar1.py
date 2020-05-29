import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../../notebooks/Data/2018WinterOlympics.csv')

print(df.head())

# data = go.Bar(x=df['NOC'],
#                 y=df['Total'])

trace1 = go.Bar(x=df['NOC'],
                y=df['Gold'],
                marker={'color':'#FFD700'},
                name='Gold')

trace2 = go.Bar(x=df['NOC'],
                y=df['Silver'],
                marker={'color':'#9EA0A1'},
                name='Silver')

trace3 = go.Bar(x=df['NOC'],
                y=df['Silver'],
                marker={'color':'#CD7F32'},
                name='Bronze')

data = [trace1,trace2,trace3]


layout = go.Layout(title='2018 Winter Olympics Tally')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='nested_bar.html')
