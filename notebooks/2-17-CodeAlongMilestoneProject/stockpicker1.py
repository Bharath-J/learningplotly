import dash
import pandas as pd
import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas_datareader as pdata
import os

app = dash.Dash()

IEX_API_KEY = os.environ.get('IEX_TOKEN')
df = pdata.iex.daily.IEXDailyReader(symbols='AAPL',api_key=IEX_API_KEY)

#print(df)
