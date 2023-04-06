import numpy as np
import matplotlib.pyplot as plt
#import pandas as pd


x1 = []
y1 = []
z1 = []
length1 = []
f = open("errormeasurement05042023.txt", 'r')
for line in f:
    x1.append(float(line.split(",")[0]))
    y1.append(float(line.split(",")[1]))
    z1.append(float(line.split(",")[2]))
f.close()


for i in range(0, len(x1)):
    length1.append(np.sqrt(x1[i]*x1[i]+y1[i]*y1[i]+z1[i]*z1[i]))

x = np.array(x1)
y = np.array(y1)
z = np.array(z1)
length = np.array(length1)


xmean = np.mean(x)
ymean = np.mean(y)
zmean = np.mean(z)
lengthmean = np.mean(length)

xvar = np.var(x)
yvar = np.var(y)
zvar = np.var(z)
lengthvar = np.var(length)

print('x', xmean, xvar)
print('y', ymean, yvar)
print('z', zmean, zvar)
print('length', lengthmean, lengthvar)
print(length)




#achman
#fig = plt.figure(1)
#ax = fig.add_subplot(projection='3d')
#ax.axis([14.34, 14.36, 51.94, 51.96, 4.18, 4.20])
#ax.scatter(x, y, z, marker='o')
#ax.scatter(xmean, ymean, zmean, marker='o', color='r')
#ax.set_xlabel('x')
#x.set_ylabel('y')
#ax.set_zlabel('z')
#plt.show()

fig2, ax2 = plt.subplots(1,3)


ax2[0].plot(x, y, 'o', label='xy')
ax2[0].plot(xmean, ymean, 'o', color='r', label='mean')
ax2[0].set_xlabel('x')
ax2[0].set_ylabel('y')
#ax2[0].set_aspect('equal', 'box')

ax2[1].plot(y, z, 'o', label='yz')
ax2[1].plot(ymean, zmean, 'o', color='r', label='mean')
ax2[1].set_xlabel('y')
ax2[1].set_ylabel('z')
#ax2[1].set_aspect('equal', 'box')

ax2[2].plot(z, x, 'o', label='zx')
ax2[2].plot(zmean, xmean, 'o', color='r', label='mean')
ax2[2].set_xlabel('z')
ax2[2].set_ylabel('x')
#ax2[2].set_aspect('equal', 'box')


#fig2.show()
plt.show()

