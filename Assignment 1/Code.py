#Assignment-1

#importing libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#initializing x,y lists
x=[1,2,3,4,5]
y=[0,2,4,6,8]

#resizing the graph
plt.figure(figsize=(5,4),dpi=100)

#plotting the graph
plt.plot(x,y)

#Adding Title,labels, legend to the graph
plt.title("Assignment-1 line chart of x, y")
plt.xlabel("x-axis")
plt.ylabel("y-axis")
plt.legend()
plt.show()

#Saving the graph
plt.savefig('assignment_1_graph.png',dpi=300)
