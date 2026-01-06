#analyze how diff apps consume battery to:
#                    identify high battery-draining apps,Visualize battery usage distribution,
#                 ,understand usage patterns.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data= pd.read_csv("07.csv")
print("\nData of Battery percentage:\n",data)

#Avg battery Consumption:
avg_battery_consum= round(np.mean(data["Battery_Consumed_Percent"]))
print("\nAvg Battery Percentage is(%):",avg_battery_consum)

#HIghest battery Consuming Apps:
highest_consum= data[data["Battery_Consumed_Percent"]>avg_battery_consum]
print("\nHighest consuming apps:\n",highest_consum)

#Highest time used app:
highest_time= data.loc[data["Usage_Time_Hours"].idxmax()]
print("\nHighest time used app is:\n",highest_time)

#Visualization:
#1.Bar chart: BatteryConsumption per app;
plt.bar(data["App"],data["Battery_Consumed_Percent"],color="green",edgecolor="Blue")
plt.xlabel("App",fontweight="bold")
plt.ylabel("Battery Percentage Used",fontweight="bold")
plt.title("Battery Percentage Used Per App",fontweight="bold",fontsize=15,color="brown")
plt.show()

#2.Battery usage distribution :Pie chart:
plt.pie(data["Battery_Consumed_Percent"],labels=data["App"],autopct="%1.1f%%",explode=[0,0,0,0,0.1,0])
plt.title("Battery Usage Distribution",fontweight="bold",fontsize=15,color="brown")
plt.show()

#3.Scatter plot: Usage time Vs Battery Consumption:
plt.scatter(data["Usage_Time_Hours"],data["Battery_Consumed_Percent"],alpha=0.4,color="blue")
plt.title("Usage time Vs Battery Consumption",fontweight="bold",fontsize=15,color="brown")
plt.xlabel("Time in Hrs",fontweight="bold")
plt.ylabel("Battery Consumed",fontweight="bold")
plt.grid()
plt.show()