import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.offline as pyo

df = pd.read_csv('../../notebooks/Data/2010YumaAZ.csv')

print(df.head())

days = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY']

data = []

# data = [go.Scatter(x=df['LST_TIME'],
#             y=df[df['DAY']==day]['T_HR_AVG'],
#             mode='lines',
#             name=day) for day in days]

for day in days:
    trace = go.Scatter(x=df['LST_TIME'],
                        y=df[df['DAY']==day]['T_HR_AVG'],
                        mode='lines',
                        name=day)
    data.append(trace)

layout = go.Layout(title='Daily Temparatures from June 1-7, Yuma, Arizona')

fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='temperature.html')
