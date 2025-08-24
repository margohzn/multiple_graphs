import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(1,90,90)
y1 = np.sin(x)
y2 = np.cos(x)

#creating multiple line plots
figure,figtable = plt.subplots(3,2,figsize = (10,9))
figure.suptitle("Multiple line plots")


histogram_data = np.random.randn(1000)
figtable[0,0].hist(histogram_data, color = "orange", edgecolor = "black", bins = 50)
figtable[0,0].set_title("Histogram:")

figtable[0,1].plot(x,y1, label = "Sin of X", color = "blue")
figtable[0,1].plot(x,y2, label = "Cos of X", color = "green")
figtable[0,1].legend(loc = "upper left")
figtable[0,1].set_title("Line graph:")

#stack plot
days = [1,2,3,4,5]
sleeping_hours = [8,7,9,6,5]
eating_hours = [2,3,1,2,4]
playing_hours = [1,1,2,1,3]
working_hours = [6,8,6,7,8]
activities = ["Sleeping", "Eating", "Playing", "Working"]

figtable[1,0].stackplot(days, sleeping_hours, eating_hours, playing_hours, working_hours, labels = activities)
figtable[1,0].set_title("Stack plot:")
figtable[1,0].legend()

#piehcart
hours = [8,2,1,8]
figtable[1,1].pie(hours, labels = activities, startangle = 45)
figtable[1,1].set_title("Pie chart")

#scatter plot
x = np.random.rand(50)
y = np.random.rand(50)
colors = np.random.rand(50)
size = 1000*np.random.randn(50)

figtable[2,0].scatter(x,y, c = colors, s = size)
figtable[2,0].set_title("Scatter plot")

#box plot 
box_data = np.random.randn(100)

figtable[2,1].boxplot(box_data)
figtable[2,1].set_title("Box plot")

plt.show()