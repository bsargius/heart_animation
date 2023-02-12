import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure() # creates figure object think of this like creating a canvas
ax = plt.axes(xlim=(0, 8), ylim=(0, 8)) # sets the boundaries of the axes of the canvas
line, = ax.plot([], [], lw=2) #creates line object that will be modified in the animation
line.set_color("red")

def init():
    line.set_data([], [])
    return line,

def animate(i):
    # creates numpy array of 20000 equally spaced values between 2.6 and 5.4 
    # this essentially creates the bounds on the x axis of the heart
    x = np.linspace(2.6, 5.4, 20000)
    y = 4 + (abs(4-x)**(2/3) + ((0.9 * abs(2-abs(4-x)**2)**(1/2)) * np.sin(np.pi * i * x)))
    line.set_data(x, y)
    return line,


anim = animation.FuncAnimation(fig, animate, init_func=init, frames=50, interval=50, blit=True)

plt.show()