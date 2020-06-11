import plotly.offline as pyo
import plotly.figure_factory as ff
import plotly.graph_objs as go
import numpy as np

#x = np.random.randn(1000)
#hist_data = [x]
#group_labels = ['distplot']

x1 = np.random.randn(200)-2
x2 = np.random.randn(200)
x3 = np.random.randn(200)+2
x4 = np.random.randn(200)+4

hist_data = [x1,x2,x3,x4]
group_labels = ['X1','X2','X3','X4']

fig = ff.create_distplot(hist_data,group_labels)
pyo.plot(fig, filename='Dist-4-variables.html')
