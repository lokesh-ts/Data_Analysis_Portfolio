#Analyze daily internet usage to: Study usage trends,Comapare weekday vs weekend usage,
#                              ,Visualize distribution & patterns.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("03.csv")
#converting of date to datetime
data["Date"]= pd.to_datetime(data["Date"])
print("\nInternet Usage data:\n",data)

#avg usage by day_type:
day_type_usage= data.groupby("Day")["Usage_GB"].mean()
print("\nDay type usage:\n",day_type_usage)

#Visualization:
#1.Daily usage trends:Line plot
x1=data["Date"]
y1=data["Usage_GB"]
plt.plot(x1,y1,linestyle="dashed",marker="o")
plt.xlabel("Date",fontweight="bold")
plt.ylabel("GB Used",fontweight="bold")
plt.title("Daily usage trends",fontsize=15,fontweight="bold",color="Grey")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#2.Weekday Vs Weekend: Bar chart
x2= day_type_usage.index
y2=day_type_usage.values
plt.bar(x2,y2,color="green",edgecolor="black")
plt.title("Comparision of Day type usages",fontsize=13,fontweight="bold")
plt.xlabel("Day Type",fontweight="bold")
plt.ylabel("Avg GB used",fontweight="bold")
plt.show()

#3.Usage distribution: Box Plot
plt.boxplot(data["Usage_GB"])   #check in notes abt box plot.
plt.ylabel("Usage(GB)")
plt.title("Interent usage distribution")
plt.show()