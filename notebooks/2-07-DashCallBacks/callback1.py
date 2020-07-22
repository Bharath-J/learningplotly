import dash
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

app = dash.Dash()

app.layout = html.Div([
            dcc.Input(id='my-id', value='Initial Text',type='text'),
            html.Div(id='my-div')
])

@app.callback(Output(component_id='my-div',component_property='children'))
def update_output_div(input_value):
    return "You entered: {}".format(input_value)

if __name__ =='__main__':
  app.run_server()
