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

xs = np.arange(-5,5,0.25)
ys = np.arange(-5,5,0.25)
X, Y = np.meshgrid(xs, ys)
R = np.sqrt(X**2 + Y**2)
Z = np.sin(R)

fig = plt.figure()
ax1 = fig.add_subplot(1, 1, 1, projection='3d')

def genData():
    pso = PSO()
    pso.genPoints(10,-4, 4, -4, 4)
    print(pso.points)
    pso.adjustZ(xs, ys, Z)
    print(pso.points)
    return pso

def genChart(pso):
    #pso.step()
    p_xs = []
    p_ys = []
    p_zs = []
    for p in pso.points:
        p_xs.append(p.x)
        p_ys.append(p.y)
        p_zs.append(p.z)
    surf = ax1.plot_surface(X, Y, Z, alpha = 0.4)
    scatter = ax1.scatter(p_xs, p_ys, p_zs, c = '#FF0000', s=30)
    plt.show()

def __main__():
    pso = genData()
    genChart(pso)
__main__()

