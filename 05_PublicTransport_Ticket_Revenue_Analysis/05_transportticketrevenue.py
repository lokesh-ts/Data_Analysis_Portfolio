#public transport ticket revenue analysis:
#Analyze ticket sales data to: calculate daily revenue,find route-wise revenue,
#                    ,identify peak revenue routes,visualize revenue trends.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("05.csv")
#converting date to datetime:
data["Date"]= pd.to_datetime(data["Date"])
print("\nData of transport revenue:\n",data)

#revenue column:
data["Revenue"]= data["Tickets_Sold"]*data["Ticket_Price"]
print("\nData after addiing revenue column:\n",data)

#Route-wise total revenue:
Route_wise_revenue= data.groupby("Route")["Revenue"].sum()
print("\nRoute-wise Revenue:\n",Route_wise_revenue)
print("\nPeak revenue route is:",Route_wise_revenue.idxmax())

#Daily revenue:
daily_revenue= data.groupby("Date")["Revenue"].sum()
print("\nDaily Revenue:\n",daily_revenue)

#Visualization:
#1.Bar chart: Route-wise revenue:
plt.bar(Route_wise_revenue.index,Route_wise_revenue.values,color="green",edgecolor="black")
plt.title("Route-wise revenue",fontsize=15,fontweight="bold",color="blue")
plt.xlabel("Route",fontweight="bold")
plt.ylabel("Revenue",fontweight="bold")
plt.show()

#2.Line Plot: Daily Revenue trend:
plt.plot(daily_revenue.index,daily_revenue.values,linestyle="dashed",marker="o")
plt.title("daily revenue trend",fontweight="bold",fontsize=15)
plt.xlabel("Date",fontweight="bold")
plt.ylabel("Revenue",fontweight="bold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()

#3.Histogram: Revenue Distribution:
plt.hist(data["Revenue"],bins=5,edgecolor="black")
plt.xlabel("Revenue",fontweight="bold")
plt.ylabel("Frequency",fontweight="bold")
plt.title("Revenue Distribution",fontweight="bold",fontsize=15,color="purple")
plt.show()