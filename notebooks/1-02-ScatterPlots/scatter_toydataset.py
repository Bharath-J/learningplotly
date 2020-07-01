import plotly.offline as pyo
import plotly.graph_objs as go
from sklearn import datasets
import pandas as pd

data = datasets.load_iris()
df = pd.DataFrame(data['data'], columns=data['feature_names'])
df['target'] = data['target']
#print(data)

x_data = df['sepal length (cm)']
y_data = df['sepal width (cm)']
color_data = [0,1,2]

# plotly_data = [go.Scatter(x=x_data,
#                             y=y_data,
#                             mode='markers',
#                             marker=dict(
#                                 size=12,
#                                 color=df['target']
#                                 ),
#                             name=color_data
#                             ) ]
plotly_data = [go.Scatter(x=df[df['target']==item]['sepal length (cm)'],
                        y=df[df['target']==item]['sepal width (cm)'],
                        mode='markers',
                        name=item,
                        marker=dict(
                            size=12
                        )
                        )
                        for item in color_data]


layout = go.Layout(title='Iris Sepal Length vs Sepal Width',
                    xaxis={'title':'Sepal Length'},
                    yaxis={'title':'Sepal Width'},
                    hovermode='closest'
                    )

fig = go.Figure(data=plotly_data, layout=layout)
# #print(help(go.Scatter))
#
pyo.plot(fig,filename='Iris_scatter.html')
