#Analyze player performance to: Compare runs scored by players,Analyze strike rate,
#                ,identify top-performing players,Visualize performance patterns.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data=pd.read_csv("09.csv")
print("\nSports Performance Data:\n",data)

#Avg runs scored:
avg_runs=np.round(np.mean(data["Runs"]),2)
print("\nAvg runs:",avg_runs)
#Adding Avg for each player:
data["Avg"]=round(data["Runs"]/data["Matches"])
print("Data After Adding Avg Column:\n",data)

#Top run'Scorer:
top_scorer=data.loc[data["Runs"].idxmax()]
print("\nTop Run Scorer is :\n",top_scorer)

#Highest Strike rate players:
high_strike_players=data[data["Strike_Rate"]>data["Strike_Rate"].mean()]
print("\nHighest Strike Rate Players:\n",high_strike_players)

#Visualization:
#1.Runs Scored by Players: Bar chart:
plt.bar(data["Player"],data["Runs"],color="green",edgecolor="blue")
plt.xlabel("Player",fontweight="bold")
plt.ylabel("Runs Scored",fontweight="bold")
plt.title("Runs Scored By Players",fontweight="bold",color="Brown",fontsize=14)
plt.show()

#2.Strike Rate Comparision:Line plot:
plt.plot(data["Player"],data["Strike_Rate"],linestyle="dotted",color="black",marker="*")
plt.xlabel("Player",fontweight="bold")
plt.ylabel("Strike Rate",fontweight="bold")
plt.title("Strike Rate Comparision",fontweight="bold",color="Brown",fontsize=14)
plt.grid()
plt.show()

#3.Runs Vs Strike rate: Scatter Plot:
plt.scatter(data["Runs"],data["Strike_Rate"],color="blue",alpha=0.3,s=200)
plt.xlabel("Runs Scored",fontweight="bold")
plt.ylabel("Strike Rate",fontweight="bold")
plt.title("Runs Vs Strike rate",fontweight="bold",color="Brown",fontsize=14)
plt.grid()
plt.show()