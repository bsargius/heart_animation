import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation

fig = plt.figure() # creates figure object think of this like creating a canvas
ax = plt.axes(xlim=(2.5,5.5), ylim=(2.5,6)) # sets the boundaries of the axes of the canvas
line, = ax.plot([], [], lw=2) #creates line object that will be modified in the animation
line2, = ax.plot([], [], lw=2)

def init():
    line.set_data([], [])
    line2.set_data([], [])
    return line, line2,

def animate(i):
    x = np.linspace(2.5,5.5, 2000)
    y = (4 + (4-x)**(2/3)) + (0.9 * (2-(4-x)**2)**(1/2)) * np.sin(np.pi * i * x)
    line.set_data(x, y)
    line2.set_data(x, -y)
    return line, line2,

anim = animation.FuncAnimation(fig, animate, init_func=init, frames=100, interval=20, blit=True)

plt.show()