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




def randomSetOfMean(counter):
    dataset=[]
    for i in range(0,counter):
        random_index = random.randint(0,len(data)-1)
        value = data[random_index]
        dataset.append(value)
    mean = statistics.mean(dataset)
    return mean

def showFig(mean_list):
    df = mean_list
    mean = statistics.mean(mean_list)
    print("Mean of Sampling Distribution: ", mean)
    # fig = ff.create_distplot([df],["temp"], show_hist=False)
    # fig.add_trace(go.Scatter(x=[mean,mean], y=[0,1], mode="lines", name="Sampling Mean"))
    # fig.show()
    
def standardDeviation():
    mean_list=[]
    for i in range(0,1000):
        set_of_means = randomSetOfMean(100)
        mean_list.append(set_of_means)
    sd = statistics.stdev(mean_list)
    print("Standard Deviation of Sampling Distribution: ", sd)



def setup():
    mean_list=[]
    for i in range(0,1000):
        set_of_means = randomSetOfMean(100)
        mean_list.append(set_of_means)
    showFig(mean_list)


setup()
standardDeviation()


## Formula
# sd of Sampling mean = sd of population/sqrt(no of data in each sample)
# Standard Error of the mean (SE)