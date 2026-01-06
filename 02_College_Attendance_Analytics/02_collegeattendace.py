#Analyze student attendance to calculate attendance percentage,identify defaulters,
#                    ,visyalize attendance distribution.

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

data= pd.read_csv("02.csv")

#calculate attendace percenatge:
data["Attendance_%"]= np.round((data["Attended_Classes"]/data["Total_Classes"])*100,2)
print("\nNew Data:\n",data)

#identify Defaulters(attendance<75%):
defaulters= data[data["Attendance_%"]<75]
print("\nDefaulters List:\n",defaulters)

#visualization:
#1.Bar chart: Attendance Percentage per student
figure, axes= plt.subplots(1,2)
x1=data["Name"]
y1= data["Attendance_%"]
axes[0].bar(x1,y1)
axes[0].set_title("Attendance Percentage per student",fontsize=10,fontweight="bold")
axes[0].set_xlabel("Name of the students",fontweight="bold")
axes[0].set_ylabel("Attendance Percentage",fontweight="bold")
#2.Histogram-Attednace distribution:
x2=data["Attendance_%"]
axes[1].hist(x2,bins=5)
axes[1].set_title("Attendance Distribution",fontsize=10,fontweight="bold")
axes[1].set_ylabel("Number of students",fontweight="bold")
axes[1].set_xlabel("Attendance Percentage",fontweight="bold")
plt.tight_layout()
plt.show()