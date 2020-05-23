import pandas as pd
import numpy as np

np.random.seed(101)

arr = np.random.randint(1,101,(20,5))
print(arr)

df = pd.DataFrame(arr)
#print(df)

df.columns = ['f1', 'f2', 'f3', 'f4', 'label']
print(df)

df2 = pd.DataFrame(np.random.randint(1, 101, (50,4)), columns=['A','B','C','D'])
print(df2)
