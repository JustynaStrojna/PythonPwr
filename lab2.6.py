import numpy as np

import matplotlib.pyplot as plt

from mpl_toolkits.mplot3d import Axes3D

#knots=wezly
from cs50 import get_int
x1 = get_int("Podaj x dla węzłów x: ")
x2 = get_int("Podaj y dla węzłów x: ")
x3 = get_int("Podaj gęstość punktów dla x: ")

y1 = get_int("Podaj y dla węzłów y: ")
y2 = get_int("Podaj y dla węzłów y: ")
y3 = get_int("Podaj gęstość punktów dla y: ")

x_knots = np.linspace(-x1*np.pi,x2*np.pi,x3) #zmiana zakresu (skali) na x

y_knots = np.linspace(-y1*np.pi,y2*np.pi,y3) #zmiana zakresu na y

X, Y = np.meshgrid(x_knots, y_knots) #siatka, pozwala na stworzenike pkt

R = np.sqrt(X**2+Y**2)

Z = np.cos(R)**2*np.exp(-0.1*R)

ax = Axes3D(plt.figure(figsize=(8,5))) # to bazowa siatka w tle

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=plt.cm.coolwarm, linewidth=0.4)

plt.show()