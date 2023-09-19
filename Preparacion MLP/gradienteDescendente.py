# -*- coding: utf-8 -*-
"""gradiente_descendente.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1ZLuf4tmm-2-A5tRlj7cg5bbf8Hxom77l
"""

from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt
import numpy as np
import math

#Definimos la Funcion
def f(x,y):
  return 10 - np.exp(-(x**2+3*y**2))

#Definimos la Derivada para X
def g1(x):
  return 2 * x * np.exp(-x**2-3*y**2)

#Definimos la Derivada para Y
def g2(y):
  return 6 * y * np.exp(-x**2-3*y**2)

plotN = 200
x = np.linspace(-2,2, plotN)
y = np.linspace(-2,2, plotN)

x, y = np.meshgrid(x,y)
z = f(x,y)

fig = plt.figure()
axis = fig.add_subplot(projection = '3d')
axis.plot_surface(x, y, z, cmap='jet', shade= "false")
plt.show()
plt.contour(x,y,z)
plt.show()

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_wireframe(x,y,z)

#gradiente
n = range(1,100)
x0 = 2
y0 = -2
h = .5

for i in n:
  x0 -= h*g1(x0)
  y0 -= h*g2(y0)

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_wireframe(x,y,z)
print("valores que optimizan la función =",x0, y0)
print("minimo en =", f(x0,y0))
