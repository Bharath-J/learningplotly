import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

df = pd.read_csv('../../notebooks/Data/OldFaithful.csv')

#print(df)

app.layout = html.Div([dcc.Graph(id='scatterplot',
                    figure = {'data':
                            [go.Scatter(
                            x=df['Y'],
                            y=df['X'],
                            mode='markers',
                            )

                            ],
                            'layout':go.Layout(title='Old Faithful',
                                                xaxis={'title':'Duration of eruption (minutes)'},
                                                yaxis={'title':'Interval to next eruption (minutes)'})


                    })

                    ])

if __name__=='__main__':
    app.run_server()
