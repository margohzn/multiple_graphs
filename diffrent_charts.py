import matplotlib.pyplot as plt 
import numpy as np 

x = np.linspace(1,90,90)
y1 = np.sin(x)
y2 = np.cos(x)

#creating multiple line plots
figure,figtable = plt.subplots(3,2,figsize = (10,10))
figure.suptitle("Multiple line plots")
plt.show()

histogram_data = np.random.randn(1000)
