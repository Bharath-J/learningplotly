import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
            dcc.Input(id='my-id', value='Initial Text',type='text'),
            html.Div(id='my-div', style={'border':'2px blue solid'})
])

if __name__ =='__main__':
  app.run_server()
