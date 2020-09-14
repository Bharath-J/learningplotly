import dash
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas_datareader.data as web
from datetime import datetime
import os
from dash.dependencies import Input,Output,State

app = dash.Dash()

IEX_API_KEY = os.environ.get('IEX_TOKEN')
#print(IEX_API_KEY)
#start = datetime(2017,1,1)
#end = datetime(2017,12,31)
#df = web.DataReader('TSLA','iex',start,end,api_key=IEX_API_KEY)
#help(web.DataReader)

app.layout = html.Div([
                    html.H1('Stock Ticker Dashboard'),
                    html.H3('Enter a stock symbol'),
                    dcc.Input(id='my_stock_picker',
                                value='TSLA'),
                    dcc.Graph(id='my_graph',
                                    figure={'data':[
                                            {'x':[1,2],'y':[3,1]}
                                    ],'layout':{'title':'Default Title'}}
                                    )
])

@app.callback(Output('my_graph','figure'),
            [Input('my_stock_picker','value')])
def update_graph(stock_ticker):
    start = datetime(2020,1,1)
    end = datetime(2020,12,31)
    df = web.DataReader(stock_ticker,'iex',start,end,api_key=IEX_API_KEY)
    fig = {'data':[{'x':df.index,'y':df['close']}],
            'layout':{'title':stock_ticker}
    }
    return fig

if __name__=='__main__':
    app.run_server()


#print(df)
