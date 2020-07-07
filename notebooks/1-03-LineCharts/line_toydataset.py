import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
from sklearn import datasets

df = pd.read_csv('../../notebooks/Data/flights.csv')

df_groupby = df.groupby(['year']).sum().reset_index()
#print(df.head())

print(df_groupby)
plotly_data = [go.Scatter(x=df_groupby['year'],
                        y=df_groupby['passengers'],
                        mode='lines+markers',
                        marker = dict(
                            size=12,
                            color='rgb(99,184,255)',
                            line=dict(
                                width=1.5
                            )
                        )
                        )]

layout = go.Layout(title='Num of Passengers per Year',
                    xaxis=dict(title='Year'),
                    yaxis=dict(title='Number of Passengers'),
                    hovermode='closest')

fig = go.Figure(data=plotly_data, layout=layout)

pyo.plot(fig,filename='Flight_Passenger.html')
