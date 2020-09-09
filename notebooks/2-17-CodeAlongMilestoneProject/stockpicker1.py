import dash
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas_datareader.data as web
from datetime import datetime
import os

app = dash.Dash()

IEX_API_KEY = os.environ.get('IEX_TOKEN')
print(IEX_API_KEY)
start = datetime(2017,1,1)
end = datetime(2017,12,31)
df = web.DataReader('TSLA','iex',start,end,api_key=IEX_API_KEY)
#help(web.DataReader)


print(df)
