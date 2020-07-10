import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
from sklearn import datasets

data = datasets.load_wine()
df = pd.DataFrame(data=['data'], columns=data['feature_names'])
