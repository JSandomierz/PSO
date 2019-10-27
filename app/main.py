import plotly.graph_objs as go
import time
import random
import numpy as np

import matplotlib
matplotlib.use('TKAgg')
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.animation as animation

from app.pso import PSO

SIZE=5
STEP = 0.05
ANIMATION_INTERVAL = 1000#ms

#PSO attributes
NUM_POINTS = 100
MOMENTUM = 0.8
LOCAL_VELOCITY = 0.2
GLOBAL_VELOCITY = 0.5

xs = np.arange(-SIZE,SIZE,STEP)
ys = np.arange(-SIZE,SIZE,STEP)
X, Y = np.meshgrid(xs, ys)

#Z = np.sin(np.sqrt(X**2 + Y**2))
#Reversed Himmelbau's function
Z = -1 * (np.square(X*X + Y - 11) + np.square(X + Y*Y - 7))
#eggholder
#Z = -1 * ((-1 * (Y + 47)) * np.sin(np.sqrt(np.abs(X/2 + (Y + 47)))) - X * np.sin(np.abs(X - (Y + 47))))

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1, projection='3d')

def genData():
    pso = PSO(momentum=MOMENTUM, localSpeed=LOCAL_VELOCITY, globalSpeed=GLOBAL_VELOCITY)
    pso.genPoints(NUM_POINTS,-SIZE+STEP, SIZE-STEP, -SIZE+STEP, SIZE-STEP)
    print(pso.points)
    pso.adjustZ(xs, ys, Z)
    print(pso.points)
    return pso

def genChart(pso):
    pso.step(xs,ys,Z)
    p_xs = []
    p_ys = []
    p_zs = []
    for p in pso.points:
        p_xs.append(p.x)
        p_ys.append(p.y)
        p_zs.append(p.z)
    #print('update')
    ax1.clear()
    #surf = ax1.plot_surface(X, Y, Z, alpha = 0.7)
    surf = ax1.plot_wireframe(X, Y, Z, alpha = 0.5)
    scatter = ax1.scatter(p_xs, p_ys, p_zs, c = '#FF0000', s=50)

def __main__():
    pso = genData()
    anim = animation.FuncAnimation(fig, lambda i: genChart(pso), interval=ANIMATION_INTERVAL)
    plt.show()
__main__()

