import pandas as pd
import plotly.offline as pyo
import plotly.graph_objs as go

y = [1,14,14,15,16,18,18,19,19,20,20,23,24,26,27,27,28,29,33,54]

data = [go.Box(y=y)]

pyo.plot(data,filename='Basic-Box-Plot.html')
