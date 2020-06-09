import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go
import numpy as np
df = pd.read_csv('../../notebooks/Data/abalone.csv')

#print(df.head())

df_random_male = np.random.choice(df[df['sex']=='M']['rings'],10,replace=False)
df_random_female = np.random.choice(df[df['sex']=='F']['rings'],10,replace=False)

trace1 = go.Box(y=df_random_male, name='Male')
trace2 = go.Box(y=df_random_female, name='Female')

data = [trace1, trace2]

layout = go.Layout(title='Male vs Female Rings')

fig = go.Figure(data=data, layout=layout)
pyo.plot(fig, filename='Male_vs_Female_Box_Plot.html')
