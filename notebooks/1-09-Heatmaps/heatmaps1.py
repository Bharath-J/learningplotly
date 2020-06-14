import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd

df = pd.read_csv('../../notebooks/Data/2010SantaBarbaraCA.csv')
print(df.head())

data = [go.Heatmap(x=df['DAY'],
                    y=df['LST_TIME'],
                    z=df['T_HR_AVG'].values.tolist(),
                    colorscale='Jet')]

layout = go.Layout(title='SantaBarbara Temp Heatmap')

fig = go.Figure(data=data,layout=layout)
pyo.plot(fig, filename='Temperature-Heatmap.html')
