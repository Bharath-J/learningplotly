import pandas as pd
import plotly.graph_objs as go
import plotly.offline as pyo

df = pd.read_csv('../../notebooks/Data/mpg.csv')

#print(df.columns)

data = [go.Scatter(x=df['acceleration'],
                    y=df['weight'],
                    text=df['name'],
                    mode='markers',
                    marker=dict(size=df['displacement']/10,
                                color=df['mpg'],
                                showscale=True))
        ]

layout = go.Layout(title="Acceleration vs Weight",
                    xaxis=dict(title='Acceleration'),
                    yaxis=dict(title='Weight'),
                    hovermode='closest')
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='Bubble-Acc-vs-Weight.html')
