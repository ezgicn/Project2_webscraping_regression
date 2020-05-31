# -*- coding: utf-8 -*-
"""
Created on Sun May 31 17:36:18 2020

@author: EN
"""

###Problem1:Create a dataset that contains the values from 0 to 10 in increments of 0.01 for the 
###𝑥 value, and 𝑠𝑖𝑛(2∗𝑝𝑖∗𝑥) for the y value.
import numpy as np
import math
x = np.array([i for i in np.arange(0,11,0.01)])
xx= 2*(math.pi)*x
y= np.sin(xx)

###Using the same dataset from the previous problem, create a line chart displaying 
###𝑦 versus x. Include a title and labels for the 𝑥 and 𝑦 axis. Play with the format of the text.
import matplotlib.pyplot as plt
plt.plot(x, y)
plt.xlabel('x',fontsize = 12, weight = 'bold', color='r')
plt.ylabel('y',fontsize = 12, weight = 'bold', color='r')
plt.title('Problem2');

#Using the sine wave data set from the previous problem, create a line chart that contains grids. 
#In the x-axis we want 6 ticks at intervals of 2, i.e. 0, 2, 4 ..., 10. 
#On the 𝑦-axis we want two ticks, one at +1 and the other at -1 with the labels "Peak" and "Valley", respectively.
