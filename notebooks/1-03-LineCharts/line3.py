import pandas as pd
import numpy as np
import plotly.graph_objs as go
import plotly.offline as pyo

df = pd.read_csv('../../notebooks/Data/2010YumaAZ.csv')

print(df.head())

data = [go.Scatter(x=df['LST_TIME'],
                    y=df['T_HR_AVG'],
                    mode='lines',
                    name=day) for day in df['DAY']]

pyo.plot(data)
