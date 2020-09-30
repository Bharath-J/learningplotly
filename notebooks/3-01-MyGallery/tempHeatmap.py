import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd
import plotly.graph_objs as go
from dash.dependencies import Input, Output

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

options = [{'label':'Blues', 'value':'Blues'},
            {'label':'Reds', 'value':'Reds'},
            {'label':'Picnic', 'value': 'Picnic'},
            {'label':'Portland','value':'Portland'}]

app.layout = html.Div([
            html.Label(['Colorscale for Heatmap']),
            dcc.Dropdown(id='color_scale_dropdown',
                        options = options,
                        value = 'Blues',
                        multi=False,
                        style={"width":"50%"}
            ),
            html.Div(dcc.Graph(id='heat-map-temp',
                                figure={'data':data,'layout':layout}),
                                style={'float':'left'}
                    )
])


@app.callback(Output(component_id='heat-map-temp',component_property='figure'),
    [Input(component_id='color_scale_dropdown', component_property='value')]
)

def update_graph(color_scale_dropdown):
    dff = df
    data = [go.Heatmap(x=dff['MONTH'],
                        y=dff['DAY'],
                        z=dff['TMAX'],
                        colorscale=color_scale_dropdown)]

    layout = go.Layout(title='Max Temperature in Cupertino in 2020',
                        xaxis=dict(title='MONTH'),
                        yaxis=dict(title='DAY'))
    figure = {'data':data, 'layout':layout}

    return figure



if __name__=='__main__':
    app.run_server()

#)]
