########################################################
# Authors: Bishoy Sargius, Jeramaya Monteiro, Tommy Nguyen
# Date: 2/10/2023
# Purpose: To animate a specific sin function that when plotted at multiple steps
# will draw a heart. This is an entry for the 2023 ACM Valentine's Coding Challenge
#######################################################

import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure() # creates figure object think of this like creating a canvas
ax = plt.axes(xlim=(0, 8), ylim=(0, 8)) # sets the boundaries of the axes of the canvas
#creates line object that will be modified in the animation and the line width is set to 2
line, = ax.plot([], [], lw=2)
line.set_color("red") # sets the color of the line object to red

def init():
    line.set_data([], [])
    return line,

def animate(i): # i is the frame
    # creates numpy array of 20000 equally spaced values between 2.6 and 5.4 
    # this essentially creates the bounds on the x axis of the heart
    x = np.linspace(2.6, 5.4, 20000)
    # this is the sin function that allows us to plot of values of the function for every value
    # of x generated in the numpy array x in the line above. Original function was from an
    # instagram post however it had to be heavily modified in order to work in python and
    # most of the time was spent on working on this sin function.
    y = 4 + (abs(4-x)**(2/3) + ((0.9 * abs(2-abs(4-x)**2)**(1/2)) * np.sin(np.pi * i * x)))
    line.set_data(x, y)
    return line,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=50, blit=True)

plt.show()