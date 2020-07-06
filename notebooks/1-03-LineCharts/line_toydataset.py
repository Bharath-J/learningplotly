import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
from sklearn import datasets

data = datasets.load_boston()

df = pd.DataFrame(data['data'], columns=data['feature_names'])

#print(data)
df['TARGET'] = data['target']
print(df.head())

x_data = df['TARGET']
y_data = df['TAX']

plotly_data = [go.Scatter(x=x_data,
                        y=y_data,
                        mode='lines'
                        )]

layout = go.Layout(title='Boston Housing Prices by Avg Num Rooms')

fig = go.Figure(data=plotly_data, layout=layout)

pyo.plot(fig,filename='Boston_Housing.html')
