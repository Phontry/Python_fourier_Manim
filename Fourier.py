# -*- coding: utf-8 -*-
"""
Created on Wed Oct 23 17:16:40 2024

@author: bfarges
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation



k = 2*np.pi
dt = 0.01

xmin = 0
xmax = 3
nbx = 151

x = np.linspace(xmin, xmax, nbx)

fig = plt.figure() # initialise la figure
line, = plt.plot([], []) 
plt.xlim(xmin, xmax)
plt.ylim(-1, 1)

def animate(i): 
    t = i * dt
    y = np.cos(k*x)
    line.set_data(x, y)
    return line,
 
ani = animation.FuncAnimation(fig, animate, frames=100,
                              interval=0.01, blit=True, repeat=True)
plt.show()
