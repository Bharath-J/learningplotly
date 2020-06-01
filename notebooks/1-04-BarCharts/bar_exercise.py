import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../../notebooks/Data/mocksurvey.csv')
#print(df)
#print(df.columns)
df.rename(columns={'Unnamed: 0':"Questions"}, inplace=True)
print(df)

#Horizontal Stacked Bar
data1 = [go.Bar(y=df['Questions'],
                 x=df[col],
                 name=col, orientation='h') for col in df.columns if col!='Questions']

data2 = [go.Bar(x=df['Questions'],
                 y=df[col],
                 name=col) for col in df.columns if col!='Questions']
#print(data)

layout = go.Layout(title='Mock Survey Results',barmode='stack')
fig1 = go.Figure(data=data1, layout=layout)
fig2 = go.Figure(data=data2, layout=layout)


pyo.plot(fig1, filename='horizontal_bar_chart.html')
pyo.plot(fig2, filename='vertical_bar_chart.html')
