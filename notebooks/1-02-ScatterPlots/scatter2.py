import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np

random_x = np.random.randn(1000)
random_y = np.random.rand(1000)

data = [go.Scatter(x=random_x,
                    y=random_y,
                    mode='markers',
                    marker = dict(
                        size=12,
                        color='rgb(124,185,232)',
                        symbol='circle',
                        line={'width':2}
                    ))]



layout = go.Layout(title='Random Numbers',
                    xaxis=dict(title='Random Normal'),
                    yaxis=dict(title='Random Uniform')
                    )
fig = go.Figure(data=data,layout=layout)

pyo.plot(fig,filename='scatter2.html')
