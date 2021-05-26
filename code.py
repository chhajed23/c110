import plotly.figure_factory as ff
import plotly.graph_objects as go
import pandas as pd
import csv
import statistics
import random

df = pd.read_csv("tempdata.csv")
data = df["temp"].tolist()
population_mean = statistics.mean(data)
std_dev = statistics.stdev(data)

print("Population mean: ", population_mean)
print("Standard Deviation: ", std_dev)

# fig = ff.create_distplot([data],["temp"], show_hist=False)
# fig.add_trace(go.Scatter(x=[population_mean,population_mean], y=[0,1], mode="lines", name="Population Mean"))


# fig.show()


dataset=[]
for i in range(0,100):
    random_index = random.randint(0,len(data))
    value = data[random_index]
    dataset.append(value)
mean = statistics.mean(dataset)
sd = statistics.stdev(dataset)

print("Mean of Sample: ", mean)
print("SD of sample: ", sd)
    
    
