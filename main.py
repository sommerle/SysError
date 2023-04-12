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


DataMittwoch = OpenFile('errormeasurementMi.txt')
DataDonnerstag = OpenFile('errormeasurementDo.txt')
Datatotal = OpenFile('errormeasurement.txt')

xMi = np.array(DataMittwoch[0])
yMi = np.array(DataMittwoch[1])
zMi = np.array(DataMittwoch[2])
lengthMi = np.array(DataMittwoch[3])

xDo = np.array(DataDonnerstag[0])
yDo = np.array(DataDonnerstag[1])
zDo = np.array(DataDonnerstag[2])
lengthDo = np.array(DataDonnerstag[3])

x = np.array(Datatotal[0])
y = np.array(Datatotal[1])
z = np.array(Datatotal[2])
length = np.array(Datatotal[3])


xMiMean = np.mean(xMi)
yMiMean = np.mean(yMi)
zMiMean = np.mean(zMi)
lengthMiMean = np.mean(lengthMi)

xDoMean = np.mean(xDo)
yDoMean = np.mean(yDo)
zDoMean = np.mean(zDo)
lengthDoMean = np.mean(lengthDo)

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




print('xMimean, sigma', xMiMean, np.sqrt(np.var(xMi)))
print('yMimean, sigma', yMiMean, np.sqrt(np.var(yMi)))
print('zMimean, sigma', zMiMean, np.sqrt(np.var(zMi)))
print('lengthMimean', lengthMiMean, np.sqrt(np.var(lengthMi)))

print('xDomean, sigma', xDoMean, np.sqrt(np.var(xDo)))
print('yDomean, sigma', yDoMean, np.sqrt(np.var(yDo)))
print('zDomean, sigma', zDoMean, np.sqrt(np.var(zDo)))
print('lengthDomean', lengthDoMean, np.sqrt(np.var(lengthDo)))

print('xmean', xmean, np.sqrt(xvar))
print('ymean', ymean, np.sqrt(yvar))
print('zmean', zmean, np.sqrt(zvar))
print('lengthmean', lengthmean, np.sqrt(lengthsigma))

print('xMimean/xDomean', xMiMean/xDoMean)
print('yMimean/yDomean', yMiMean/yDoMean)
print('zMimean/zDomean', zMiMean/zDoMean)
print('length: Mimean/Domean', lengthMiMean/lengthDoMean)


#print(length)



fig = plt.figure(1)
ax = fig.add_subplot(projection='3d')
ax.scatter(x, y, z, marker='o', label='absolute distance and moved')
ax.scatter(xMi, yMi, zMi, marker='o', label='Wednesday')
ax.scatter(xDo, yDo, zDo, marker='o', color='mediumseagreen', label='Thursday')
ax.scatter(xmean, ymean, zmean, label='mean', marker='o', color='r')
ax.scatter(xMiMean, yMiMean, zMiMean, label='mean Wednesday',marker='o', color='midnightblue')
ax.scatter(xDoMean, yDoMean, zDoMean, label='mean Thursday',marker='o', color='darkgreen')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z')
ax.legend(loc='best')
#fig.plot()

fig2, ax2 = plt.subplots(1,3)

ax2[0].plot(xMi, yMi, 'o', label='Wednesday')
ax2[0].plot(xDo, yDo, 'o', color='mediumseagreen', label='Thursday')
ax2[0].plot(xmean, ymean, 'o', color='r', label='mean')
ax2[0].plot(xMiMean, yMiMean, label='mean Wednesday', marker='o', color='midnightblue')
ax2[0].plot(xDoMean, yDoMean, label='mean Thursday', marker='o', color='darkgreen')
ax2[0].axis([np.min(x)-0.0005, np.max(x)+0.0005, np.min(y)-0.0005, np.max(y)+0.0005])
ax2[0].set_xlabel('x')
ax2[0].set_ylabel('y')
ax2[0].set_title('xy')
#ax2[0].legend(loc='best')
#ax2[0].set_aspect('equal', 'box')


ax2[1].plot(xMi, zMi, 'o', label='Wednesday')
ax2[1].plot(xDo, zDo, 'o', color='mediumseagreen', label='Thursday')
ax2[1].plot(xmean, zmean, 'o', color='r', label='mean')
ax2[1].plot(xMiMean, zMiMean, label='mean Wednesday',marker='o', color='midnightblue')
ax2[1].plot(xDoMean, zDoMean, label='mean Thursday',marker='o', color='darkgreen')
ax2[1].axis([min(x)-0.0005, max(x)+0.0005, min(z)-0.0005, max(z)+0.0005])
ax2[1].set_xlabel('x')
ax2[1].set_ylabel('z')
ax2[1].set_title('xz')
#ax2[1].legend(loc='best')
#ax2[1].set_aspect('equal', 'box')


ax2[2].plot(yMi, zMi, 'o', label='Wednesday')
ax2[2].plot(yDo, zDo, 'o', color='mediumseagreen', label='Thursday')
ax2[2].plot(xmean, ymean, 'o', color='r', label='mean')
ax2[2].plot(yMiMean, zMiMean, label='mean Wednesday',marker='o', color='midnightblue')
ax2[2].plot(yDoMean, zDoMean, label='mean Thursday',marker='o', color='darkgreen')
ax2[2].axis([min(y)-0.0005, max(y)+0.0005, min(z)-0.0005, max(z)+0.0005])
ax2[2].set_xlabel('y')
ax2[2].set_ylabel('z')
ax2[2].set_title('yz')
ax2[2].legend(loc='best')
#ax2[2].set_aspect('equal', 'box')
#fig2.plot()

#fig2.show()
plt.show()