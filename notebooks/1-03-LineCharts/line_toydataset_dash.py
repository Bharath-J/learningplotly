import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.graph_objs as go
import pandas as pd

app = dash.Dash()

df = pd.read_csv('../../notebooks/Data/flights.csv')
df_groupby = df.groupby(['year']).sum().reset_index()

app.layout = html.Div([dcc.Graph(id='linechart',
                    figure=dict(
                    data=[go.Scatter(x=df_groupby['year'],
                                    y=df_groupby['passengers'],
                                    mode='lines+markers',
                                    marker=dict(
                                        size=12
                                    ))],
                    layout=go.Layout(title='Number of Passengers per Year',
                                        xaxis=dict(title='Year'),
                                        yaxis=dict(title='Number of Passengers'),
                                        hovermode='closest')

                    )
                    )])

if __name__=='__main__':
    app.run_server()
