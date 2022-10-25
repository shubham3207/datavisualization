#importing packages for data visualization
import matplotlib.pyplot as plt
import csv
#creating empty list to fetch data from csv file which will be represented in  x-axis,y-axis
x=[]
y=[]
#opening our csv file in read mode
with open("bargraph.csv", "r") as csvfile:

   plots=csv.reader(csvfile,delimiter=',')
   for row in plots:
       x.append(row[0])
       y.append(int(row[1]))
   plt.scatter(x, y, color='blue', label="red")
   plt.xlabel('Years')
   plt.ylabel('Temperatures')
   plt.title("bar graphs for temperature in different years")
   plt.xticks(rotation=25)
   #if you want to add grid
   #plt.grid()


   plt.legend()
   plt.show()
