import plotly.figure_factory as ff
import pandas as pd
import csv
import plotly.graph_objects as go
import statistics
import random

df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()

mean = sum(data) / len(data)
median = statistics.median(data)
mode = statistics.mode(data)
std = statistics.stdev(data)

first_std_start, first_std_end = mean-std_deviation, mean+std
second_std_start, second_std_end = mean-(2*std), mean+(2*std)
third_std_start, third_std_end = mean-(3*std), mean+(3*std)

fig = ff.create_distplot([data], ["reading scores"], show_hist=False)

fig.add_trace(go.Scatter(x=[mean, mean], y=[0, 0.17], mode="lines", name="MEAN"))
fig.add_trace(go.Scatter(x=[first_std_start, first_std_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[first_std_end, first_std_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 1"))
fig.add_trace(go.Scatter(x=[second_std_start, second_std_start], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))
fig.add_trace(go.Scatter(x=[second_std_end, second_std_end], y=[0, 0.17], mode="lines", name="STANDARD DEVIATION 2"))

fig.show()

lodw_1_std = [result for result in data if result > first_std_start and result < first_std_end]
lodw_2_std = [result for result in data if result > second_std_start and result < second_std_end]
lodw_3_std = [result for result in data if result > third_std_start and result < third_std_end]

print("Mean of this data is {}".format(mean))
print("Median of this data is {}".format(median))
print("Mode of this data is {}".format(mode))

print("Standard deviation of this data is {}".format(std))

print("{}% of data lies within 1 standard deviation".format(len(lodw_1_std)*100.0/len(data)))
print("{}% of data lies within 2 standard deviations".format(len(lodw_2_std)*100.0/len(data)))
print("{}% of data lies within 3 standard deviations".format(len(lodw_3_std)*100.0/len(data)))
