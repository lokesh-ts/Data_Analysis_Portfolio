import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#identify traffic hours,compare weekday vs weekend traffic,visualize traffic trends clearly

data=pd.read_csv("01.csv")
#converting of date to datetime
data["Date"]= pd.to_datetime(data["Date"])
print("\nTraffic Flow:\n")
print(data)

#avg traffic hour:
hourly_traffic= data.groupby("Hour")["Vehicle_Count"].mean()
print("\nAvg Traffic Hours:\n",hourly_traffic)

#peak traffic hour:
peak_traffic_hour=hourly_traffic.idxmax()
print("\nPeak Traffic Hour is:\n",peak_traffic_hour)

#weekday Vs Weekend traffic:
day_type_avg= data.groupby("Day")["Vehicle_Count"].mean()
print("\nweekday Vs Weekend traffic:\n",day_type_avg)
print("\nThe Highest Traffic is during",day_type_avg.idxmax())

#Visualization:
#Line plot: Avg traffic per hour:
x1=hourly_traffic.index
y1=hourly_traffic.values
plt.title("Avg Traffic Per hour",fontsize=15,fontweight="bold",color="green")
plt.xlabel("Hour of the day",fontweight="bold")
plt.ylabel("Avg vehicle count",fontweight="bold")
plt.plot(x1,y1,marker="*",markerfacecolor="black")
plt.grid(True)
plt.show()

#Bar chart:  Weekday vs Weekend:
x2=day_type_avg.index
y2=day_type_avg.values
plt.bar(x2,y2,color="skyblue",edgecolor="green")
plt.title("Weekday Vs Weekend",fontsize=15,fontweight="bold")
plt.xlabel("Days",fontweight="bold")
plt.ylabel("Vehicle count",fontweight="bold")
plt.show()

#we can also bring the same plots in a slide by using subplots
figure, axes=plt.subplots(1,2)
axes[0].plot(x1,y1)
axes[0].set_title("Avg Traffic Per hour")
axes[0].set_xlabel("Hour of the day")
axes[0].set_ylabel("Avg vehicle count")
axes[1].bar(x2,y2)
axes[1].set_title("Weekday Vs Weekend")
axes[1].set_xlabel("Days")
axes[1].set_ylabel("Vehicle count")
plt.tight_layout()
plt.show()