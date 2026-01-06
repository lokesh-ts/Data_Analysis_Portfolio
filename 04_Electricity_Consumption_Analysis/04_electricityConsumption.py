#Analyze electricity usage data to: Observe daily consumption trend,find average cosumption,
#                      ,visualize monthly usage,Identify high consumption days

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data= pd.read_csv("04.csv")
#converting date to datetime:
data["Date"]= pd.to_datetime(data["Date"])
print("\nElectricity Data:\n",data)

#Avg consumption:
avg_consumption= np.mean(data["Units_Consumed"])
print("\nAverage electricity Consumption is:",avg_consumption)

#Highly Consumed days(above average):
highly_consumed= data[data["Units_Consumed"]>avg_consumption]
print("\nHighly Consumed Days are:\n",highly_consumed)

#Visualization:
#1.Daily Electricity consumption trends: Line pLot
x1= data["Date"]
y1= data["Units_Consumed"]
plt.plot(x1,y1,marker="o",color="green",linestyle="dashed")
plt.xlabel("Date",fontweight="bold")
plt.ylabel("Units Consumed",fontweight="bold")
plt.title("Electricity consumption trends",fontsize=14,fontweight="bold",color="Blue")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#2.Electricity Consumption per day: Bar Chart
plt.bar(data["Date"].dt.strftime("%d-%b"),data["Units_Consumed"])
plt.xlabel("Date")
plt.ylabel("Units consumed")
plt.title("Daily Electricity Consumption")
plt.show()

#3.histogram- Consumption distribution:
plt.hist(data["Units_Consumed"],bins=5)
plt.xlabel("Units Consumed")
plt.ylabel("Frequency")
plt.title("Electrcity Consumption Distribution")
plt.show()