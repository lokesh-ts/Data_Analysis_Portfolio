#website traffic analysis:
#analyze website traffic data to: Understand daily visitors,compare page views Vs visitors,
#                          ,Visualize traffic trends

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data= pd.read_csv("06.csv")
#convrting date to datetime:
data["Date"]= pd.to_datetime(data["Date"])
print("\nWebsite Traffic Data:\n",data)

#Avg daily visitors:
avg_daily_visitors= data["Visitors"].mean()
print("\nAvg Daily Visitors:",avg_daily_visitors)

#Maximum visitors on a day:
print("\nMaximum Visitor on a day:\n",data.loc[data["Visitors"].idxmax()])

#Visualiaztion:
#1.Visitors trend:Line plot:
plt.plot(data["Date"],data["Visitors"],linestyle="dotted",color="black",marker="o")
plt.xlabel("Date",fontweight="bold")
plt.ylabel("Number of Visitors",fontweight="bold")
plt.title("Visitors Traffic Trend",fontweight="bold",fontsize=15)
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#Page Views Trends: Line Plot:
plt.plot(data["Date"],data["Page_Views"],linestyle="dotted",color="black",marker="o")
plt.xlabel("Date",fontweight="bold")
plt.ylabel("Number of Page Viewed",fontweight="bold")
plt.title("Page Views Trend",fontweight="bold",fontsize=15,color="brown")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#3.Visitors Vs Page Views:Scatter plot:
plt.scatter(data["Visitors"],data["Page_Views"],alpha=0.5,s=200)
plt.xlabel("Visitors",fontweight="bold")
plt.ylabel("Pages viewed",fontweight="bold")
plt.title("Visitors Vs Page Views",fontweight="bold",fontsize=15,color="brown")
plt.grid(True)
plt.show()