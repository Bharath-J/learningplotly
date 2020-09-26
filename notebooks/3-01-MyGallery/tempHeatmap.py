import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go

app = dash.Dash()

df = pd.read_csv("../../notebooks/Data/CupertinoWeather2020.csv")

df['DAY'] = pd.DatetimeIndex(df['DATE']).day
df['MONTH'] = pd.DatetimeIndex(df['DATE']).month


data = [go.Heatmap(x=df['MONTH'],
                    y=df['DAY'],
                    z=df['TMAX'],
                    colorscale='Blues')]

layout = go.Layout(title='Max Temperature in Cupertino in 2020',
                    xaxis=dict(title='MONTH'),
                    yaxis=dict(title='DAY'))

app.layout = html.Div([
            html.Div(dcc.Graph(id='heat-map-temp',
                                figure={'data':data,'layout':layout}),
                                style={'float':'left'}
                                )
])

if __name__=='__main__':
    app.run_server()

#)]
