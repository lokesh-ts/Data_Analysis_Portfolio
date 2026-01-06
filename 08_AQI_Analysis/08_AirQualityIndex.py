#AQI Category Classification(Good,Poor,Moderate..)
#Daily AQI Change(delta AQI),Most polluted city detection,Rolling avg(trend smoothing),
#        ,Adv visual insights.
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data= pd.read_csv("08.csv")
#converting date to  datetime:
data["Date"]=pd.to_datetime(data["Date"])
print("\nAQI Data:\n",data)

#AQI Category Classification:
def classify_aqi(aqi):
    if aqi<=50:
        return "Good"
    elif aqi<=100:
        return "Satisfactory"
    elif aqi<=200:
        return "Moderate"
    elif aqi<=300:
        return "Poor"
    else:
        return "Very Poor"
    
data["AQI_Category"]=data["AQI"].apply(classify_aqi)
print("\nDate with Categories:\n",data)

#Most Polluted City(Avg):
city_avg_aqi=data.groupby("City")["AQI"].mean().round(2)
most_polluted_city= city_avg_aqi.idxmax()
print("\nCities avg AQI:\n",city_avg_aqi)
print("\nMost Polltuted City is:",most_polluted_city)

#Daily AQI Change:(delta AQI):
data=data.sort_values(["City","Date"])
data["Daily_AQI_Change"]=data.groupby("City")["AQI"].diff()
print("\nAQI Change day-to-day:\n",data)

#Rolling Avg:(Smooth Trend):
data["Rolling_aqi"]=data.groupby("City")["AQI"].transform(
    lambda x:x.rolling(window=2).mean()
)
print("\nData with Rolling Avg:\n",data)

#Visualization:
#1.Avg AQI per day:
plt.bar(city_avg_aqi.index,city_avg_aqi.values,color="green")
plt.title("Avg AQI per day",fontweight="bold",fontsize=15,color="brown")
plt.xlabel("City",fontweight="bold")
plt.ylabel("Avg AQI",fontweight="bold")
plt.show()

#2.AQI Category Distribution:
data["AQI_Category"].value_counts().plot(kind="bar")
plt.xlabel("AQI Category")
plt.ylabel("Count")
plt.title("AQI Category Distribution")
plt.tight_layout()
plt.show()