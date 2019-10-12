import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

import numpy as np


fig = plt.figure()
ax1 = fig.add_subplot(1,1,1, projection='3d')

xs = np.arange(-5,5,0.25)
ys = np.arange(-5,5,0.25)
X, Y = np.meshgrid(xs, ys)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

#points
p_xs = [0, 1, 2, 3]
p_ys = [0, 1, 2, 3]
p_zs = [10 for x in p_xs]

surf = ax1.plot_surface(X,Y,Z)
scatter = ax1.scatter(p_xs, p_ys, p_zs)
"""
def animate(i):
    ax1.clear()
    xs.append(i)
    ys.append(i**2)
    ax1.plot(xs,ys)

anim = animation.FuncAnimation(fig, animate, interval=100)"""
plt.show()