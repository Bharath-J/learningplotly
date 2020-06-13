import pandas as pd
import plotly.offline as pyo
import plotly.figure_factory as ff

df = pd.read_csv('../../notebooks/Data/iris.csv')
print(df.head())

x1 = df[df['class']=='Iris-setosa']['petal_length']
x2 = df[df['class']=='Iris-virginica']['petal_length']
x3 = df[df['class']=='Iris-versicolor']['petal_length']

hist_data = [x1,x2,x3]
group_labels = ['Iris-setosa','Iris-virginica','Iris-versicolor']

fig = ff.create_distplot(hist_data,group_labels)
pyo.plot(fig, filename='Distribution-Plot-Iris-Dataset.html')
