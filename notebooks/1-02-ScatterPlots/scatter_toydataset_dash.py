import dash
import dash_core_components as dcc
import dash_html_components as html
from sklearn import datasets
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

data = datasets.load_iris()
df = pd.DataFrame(data['data'], columns=data['feature_names'])
df['target'] = data['target']
df['target_names'] = ['setosa' if item==0 else 'versicolor' if item==1 else 'virginica'
                        for item in df['target']]
print(df)

x_data = df['sepal length (cm)']
y_data = df['sepal width (cm)']
color_data = ["setosa","versicolor","virginica"]

app.layout = html.Div([dcc.Graph(id='scatterplot',
                    figure = {'data':
                    [go.Scatter(x=df[df['target_names'] == item]['sepal length (cm)'],
                                y=df[df['target_names']== item]['sepal width (cm)'],
                                mode='markers',
                                name=item,
                                marker=dict(
                                            size=12
                                            )
                                )
                                for item in color_data],
                                'layout':
                                go.Layout(title='Iris Sepal Length vs Sepal Width',
                                            xaxis={'title':'Sepal Length'},
                                            yaxis={'title':'Sepal Width'},
                                            hovermode='closest'
                                            )

                    }

                        )])

if __name__=='__main__':
    app.run_server()
