import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../../notebooks/Data/mpg.csv')

#print(df.columns)
#print(help(go.Scatter))

data =[go.Scatter(x=df['horsepower'],
                    y=df['mpg'],
                    text=df['name'],
                    mode='markers',
                    marker=dict(size=df['weight']/200,
                                color=df['cylinders'],
                                showscale=True))]
layout = go.Layout(title='Bubble Chart',
                    xaxis=dict(title='Horsepower'),
                    yaxis=dict(title='MPG'),
                    hovermode="closest")
fig = go.Figure(data=data, layout=layout)
pyo.plot(fig,filename='Bubble-HP-vs-MPG.html')
