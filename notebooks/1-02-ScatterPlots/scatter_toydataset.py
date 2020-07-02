import plotly.offline as pyo
import plotly.graph_objs as go
from sklearn import datasets
import pandas as pd

data = datasets.load_iris()
df = pd.DataFrame(data['data'], columns=data['feature_names'])
df['target'] = data['target']
df['target_names'] = ['setosa' if item==0 else 'versicolor' if item==1 else 'virginica'
                        for item in df['target']]
print(df)

x_data = df['sepal length (cm)']
y_data = df['sepal width (cm)']
color_data = ["setosa","versicolor","virginica"]

plotly_data = [go.Scatter(x=df[df['target_names'] == item]['sepal length (cm)'],
                        y=df[df['target_names']== item]['sepal width (cm)'],
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

pyo.plot(fig,filename='Iris_scatter.html')
