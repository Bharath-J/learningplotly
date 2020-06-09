import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../../notebooks/Data/mpg.csv')

#print(df.head())
data = [go.Histogram(x=df['mpg'], xbins=dict(size=5))]
layout = go.Layout(title='MPG Histogram')
fig = go.Figure(data=data,layout=layout)
pyo.plot(fig, filename='mpg_histogram.html')
