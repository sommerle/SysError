import numpy as np
import matplotlib.pyplot as plt




def OpenFile(filename):
    x1 = []
    y1 = []
    z1 = []
    length1 = []
    f = open(filename, 'r')
    for line in f:
        x1.append(float(line.split(",")[0]))
        y1.append(float(line.split(",")[1]))
        z1.append(float(line.split(",")[2]))
    f.close()
    for i in range(0, len(x1)):
        length1.append(np.sqrt(x1[i]*x1[i]+y1[i]*y1[i]+z1[i]*z1[i]))
    return x1, y1, z1, length1


Datatotal = OpenFile('errorsys190423.txt')


x = np.array(Datatotal[0])
y = np.array(Datatotal[1])
z = np.array(Datatotal[2])
length = np.array(Datatotal[3])


xmean = np.mean(x)
ymean = np.mean(y)
zmean = np.mean(z)
lengthmean = np.mean(length)

xvar = np.var(x)
yvar = np.var(y)
zvar = np.var(z)
lengthvar = np.var(length)

xsigma = np.sqrt(xvar)
ysigma = np.sqrt(yvar)
zsigma = np.sqrt(zvar)
lengthsigma = np.sqrt(lengthmean)



print('xmean', xmean, np.sqrt(xvar))
print('ymean', ymean, np.sqrt(yvar))
print('zmean', zmean, np.sqrt(zvar))
print('lengthmean', lengthmean, np.sqrt(lengthsigma))




fig = plt.figure(1)
ax = fig.add_subplot(projection='3d')
ax.scatter(x, y, z, marker='o', label='absolute distance and moved')
ax.scatter(xmean, ymean, zmean, label='mean', marker='o', color='r')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.legend(loc='best')


fig2, ax2 = plt.subplots(1,3)

ax2[0].plot(x, y, 'o', label='absolute distance and moved')
ax2[0].plot(xmean, ymean, 'o', color='r', label='mean')
ax2[0].axis([np.min(x)-0.0005, np.max(x)+0.0005, np.min(y)-0.0005, np.max(y)+0.0005])
ax2[0].set_xlabel('x')
ax2[0].set_ylabel('y')
ax2[0].set_title('xy')
#ax2[0].legend(loc='best')
#ax2[0].set_aspect('equal', 'box')


ax2[1].plot(x, z, 'o', label='absolute distance and moved')
ax2[1].plot(xmean, zmean, 'o', color='r', label='mean')
ax2[1].axis([min(x)-0.0005, max(x)+0.0005, min(z)-0.0005, max(z)+0.0005])
ax2[1].set_xlabel('x')
ax2[1].set_ylabel('z')
ax2[1].set_title('xz')
#ax2[1].legend(loc='best')
#ax2[1].set_aspect('equal', 'box')


ax2[2].plot(y, z, 'o', label='absolute distance and moved')
ax2[2].plot(xmean, ymean, 'o', color='r', label='mean')
ax2[2].axis([min(y)-0.0005, max(y)+0.0005, min(z)-0.0005, max(z)+0.0005])
ax2[2].set_xlabel('y')
ax2[2].set_ylabel('z')
ax2[2].set_title('yz')
ax2[2].legend(loc='best')
#ax2[2].set_aspect('equal', 'box')


plt.show()