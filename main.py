import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


x1 = []
y1 = []
z1 = []
f = open("errormeasurement05042023.txt", 'r')
for line in f:
    x1.append(float(line.split(",")[0]))
    y1.append(float(line.split(",")[0]))
    z1.append(float(line.split(",")[0]))
f.close()
x = np.array(x1)
y = np.array(y1)
z = np.array(z1)


xmean = np.mean(x)
ymean = np.mean(y)
zmean = np.mean(z)

xvar = np.var(x)
yvar = np.var(y)
zvar = np.var(z)



#achman
fig = plt.figure()
ax = fig.add_subplot(projection='3d')
ax.axis([14.34, 14.36, 51.94, 51.96, 4.18, 4.20])
ax.scatter(x, y, z, marker='.')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
plt.show()



