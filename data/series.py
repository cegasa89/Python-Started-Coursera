import numpy as np
import pandas as pd

x = ['a', 'b', 'c', 'd', 'e']
y = [1, 2, 3, 4, 5]
z= {1:'a', 2:'b', 3:'c', 4:'d', 5:'e', }

#a = pd.Series(data = x, index = y )
a = pd.Series(x, y )
print(a)
print(a[:2])