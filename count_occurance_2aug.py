import pandas as pd

#declaring the list
l = [1, 1, 2, 2, 2, 3, 3, 4, 4, 5, 5]

count = pd.Series(l).value_counts()
print(count)