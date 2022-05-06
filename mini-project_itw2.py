%matplotlib inline
import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

recent_grads = pd.read_csv('recent-grads.csv')
recent_grads.info()
recent_grads.head()

recent_grads.describe()
print('Petroleum Engineering overview')
recent_grads.iloc[0]
raw_data_count = recent_grads.shape[0]
recent_grads = recent_grads.dropna()
cleaned_data_count = recent_grads.shape[0]
print('Cleaned data count: ', cleaned_data_count)
print('Raw data count: ', raw_data_count)
ax = recent_grads.plot(x='Total', y='Median', kind='scatter')
ax.set_title('Total number of graduates vs. Median')
recent_grads.plot(x = 'Total', y = 'Unemployment_rate', kind = 'scatter',
                 title = 'Total number of graduates vs. Unemployment Rate')
recent_grads.plot(x = 'Full_time', y = 'Median', kind = 'scatter',
                 title = 'Number of Full Time Workers vs. Median')
recent_grads.plot(x = 'ShareWomen', y = 'Unemployment_rate', kind = 'scatter',
                 title = 'Share of Women vs. Unemployment Rate')
recent_grads['Sample_size'].hist(bins = 25)
plt.title('Histogram of sample size of graduates')
recent_grads['Median'].hist(bins = 20)
plt.title('Histogram of median of graduates')
recent_grads['Unemployment_rate'].hist(bins = 25)
plt.title('Histogram of unemployment rate of graduates per major')
recent_grads[-20:].plot.bar(x='Major', y='ShareWomen')
plt.title('Participation of Women Across Majors - Arts, Education and Humanities')
