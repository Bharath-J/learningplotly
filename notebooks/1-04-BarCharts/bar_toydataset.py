import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
from sklearn import datasets

data = datasets.load_wine()
df = pd.DataFrame(data['data'], columns=data['feature_names'])
df['target']=data['target']
df['target_names']=['class_0' if item==0 else 'class_1' if item==1 else 'class_2'
                    for item in df['target']]
print(df.head())
print(df.columns)

df_groupby = df.groupby(['target_names']).mean().reset_index()
print(df_groupby.head())

trace1 = go.Bar(x=df_groupby['target_names'],
                y=df_groupby['alcohol'],
                )

data = [trace1]

layout = go.Layout(title='Mean Alcohol Level',
                    xaxis=dict(title='Alcohol Category'),
                    yaxis=dict(title='Mean Alcohol Level'))
fig = go.Figure(data=data, layout=layout)

pyo.plot(fig, filename='bar_mean_alcohol.html')
