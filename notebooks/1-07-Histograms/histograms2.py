import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

df = pd.read_csv('../../notebooks/Data/abalone.csv')

print(df.head())

data = [go.Histogram(x=df['length'],xbins=dict(start=0, end=1, size=0.02))]
layout = go.Layout(title='Histogram of Abalone Lengths')
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='Hist_Abalone_Length.html')
