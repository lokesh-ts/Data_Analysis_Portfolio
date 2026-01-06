#Anayze Movie Collection data: Compare collections of movies, track daily box office trend,
#       ,Identify highest grossing movie,understand collection distribution.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data= pd.read_csv("10.csv")
#Converting date to datetime:
data["Date"]=pd.to_datetime(data["Date"])
print("\nMovies Box Office Collection Data:\n",data)

#total collection per movie:
total_collection= data.groupby("Movie")["Collection_Crore"].sum()
print("Total Collection For each Movie(Crore) is:\n",total_collection)

#Highest Grossing Movie:
Highest_gross_movie= total_collection.idxmax()
print("\nHighest grossing Movie is:",Highest_gross_movie)

#daily avg Collection:
daily_avg= data.groupby("Date")["Collection_Crore"].mean().round(2)
daily_avg=daily_avg.sort_index()
print("\nDaily Avg Collection:\n",daily_avg)

#Visualization:
#1.Total Collection Movie:Bar Chart:
plt.bar(total_collection.index,total_collection.values,color="green")
plt.xlabel("Movie")
plt.ylabel("Total Collection(Crores)")
plt.title("Total Collection Per Movie",fontsize=14,fontweight="bold")
plt.show()

#2.Daily Avg Box office Trend:Line Plot:
plt.plot(daily_avg.index,daily_avg.values,color="blue",marker="o")
plt.xlabel("Date")
plt.ylabel("Avg Collection(Crores)")
plt.title("Daily Avg Box office Trend",fontsize=14,fontweight="bold")
plt.xticks(rotation=45)
plt.tight_layout()
plt.grid()
plt.show()

#3.Collection Distribution:
plt.hist(data["Collection_Crore"],bins=5,edgecolor="blue")
plt.xlabel("Collection(Crores)")
plt.ylabel("Frequency")
plt.title("Collection Distribution")
plt.show()