import plotly.offline as pyo
import plotly.graph_objs as go
import pandas as pd
from sklearn import datasets

data = datasets.load_wine()
df = pd.DataFrame(data['data'], columns=data['feature_names'])
df['target']=data['target']
df['target_names']=['class_0' if item==0 else 'class_1' if item==1 else 'class_2'
                    for item in df['target']]
print(df.head())
print(df.columns)
