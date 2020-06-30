import plotly.offline as pyo
import plotly.graph_objs as go
from sklearn import datasets
import pandas as pd

data = datasets.load_iris()
df = pd.DataFrame(data['data'], columns=data['feature_names'])
df['target'] = data['target']
print(df.head())

x_data = df['sepal length (cm)']
y_data = df['sepal width (cm)']
color_data = df['target']

plotly_data = [go.Scatter(x=x_data,
                            y=y_data,
                            mode='markers',
                            name=item,
                            marker=dict(
                                size=12,
                                color=color_data,
                                symbol='circle',
                                line={'width':2}
                            )) for item in color_data]

layout = go.Layout(title='Iris Sepal Length vs Sepal Width',
                    xaxis={'title':'Sepal Length'},
                    yaxis={'title':'Sepal Width'},
                    hovermode='closest'
                    )

fig = go.Figure(data=plotly_data, layout=layout)
#print(help(go.Scatter))

pyo.plot(fig,filename='Iris_scatter.html')
