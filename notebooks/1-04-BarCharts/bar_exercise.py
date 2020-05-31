import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../../notebooks/Data/mocksurvey.csv')
print(df.head())

#trace1 = go.Bar(x=df['Unnamed:0'])
