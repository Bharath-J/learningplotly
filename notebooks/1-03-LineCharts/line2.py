import pandas as pd
import numpy as np
import plotly.offline as pyo
import plotly.graph_objs as go

df = pd.read_csv('../../notebooks/SourceData/nst-est2017-alldata.csv')
#print(df)

df2 = df[df['DIVISION'] == '1']
df2.set_index('NAME',inplace=True)
print(df2)

list_of_pop_col = [col for col in df2.columns if col.startswith('POP')]
df2 = df2[list_of_pop_col]

#print(df2)
#print(df2.columns)

data = [go.Scatter(x=df2.columns,
                    y=df2.loc[name],
                    mode='lines+markers',
                    name=name) for name in df2.index]

layout = go.Layout(title='Population Estimate of N.E. States')
fig = go.Figure(layout=layout, data=data)

pyo.plot(fig,filename='population_estimate.html')
