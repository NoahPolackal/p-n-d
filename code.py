import plotly.figure_factory as ff
import pandas as pd
import csv
import statistics
import plotly.graph_objects as go
import random

df = pd.read_csv("StudentsPerformance.csv")
data = df["reading score"].tolist()

mean = sum(data) / len(data)
median = statistics.median(data)
mode = statistics.mode(data)
std = statistics.stdev(data)

first_std_start, first_std_end = mean-std, mean+std
second_std_start, second_std_end = mean-(2*std), mean+(2*std)
third_std_start, third_std_end = mean-(3*std), mean+(3*std)

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
