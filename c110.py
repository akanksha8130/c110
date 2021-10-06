import pandas as pd
import statistics
import plotly.figure_factory as ff

df=pd.read_csv('data.csv')
data=df['temp'].tolist()

population_mean=statistics.mean(data)
std_dev=S
fig=ff.create_distplot([data],['temp'],show_hist=False)
fig.show()