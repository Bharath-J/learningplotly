import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd
from numpy import random

app = dash.Dash()

df = pd.read_csv('../../notebooks/Data/mpg.csv')
# Adding noise, adding jitter
df['year'] = random.randint(-4,5,len(df))*0.1 + df['model_year']

app.layout = html.Div([
                    dcc.Graph(id='mpg-scatter',
                                figure={
                                'data':[go.Scatter(
                                        x=df['year']+1900,
                                        y=df['mpg'],
                                        text = df['name'],
                                        hoverinfo = 'text',
                                        mode = 'markers'
                                )],
                                'layout':go.Layout(title='MPG Data',
                                xaxis={'title':'Model Year'},
                                yaxis={'title':'MPG'},
                                hovermode='closest')
                                }
                    )

])


if __name__=='__main__':
    app.run_server(port=8081)
