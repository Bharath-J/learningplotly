import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
from plotly import tools

df = pd.read_csv("../../notebooks/Data/flights.csv")
print(df.head())

data = [go.Heatmap(x=df['year'],
                  y=df['month'],
                  z=df['passengers'],
                  colorscale='Jet')]
layout = go.Layout(title='Passenger Density in Flights')
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig,filename='Passenger_Density.html')
