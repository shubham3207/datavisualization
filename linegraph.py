import matplotlib.pyplot as plt
import csv
x=[]
y=[]

with open("practicedata.csv", "r") as csvfile:

   plots=csv.reader(csvfile,delimiter=',')
   for row in plots:
       x.append(row[0])
       y.append(int(row[2]))
   plt.plot(x, y, color='blue', label="age",marker='o',linestyle='dashed')
   plt.xlabel('Names')
   plt.ylabel('Ages')
   plt.title("line graphs for name and ages of different people")

   plt.grid()
   plt.legend()
   plt.show()


