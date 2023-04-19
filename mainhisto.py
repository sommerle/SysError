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



#print(length)

fig2, ax2 = plt.subplots(1,3)

ax2[0].hist(x, 10, label='x')
ax2[0].set_xlabel('x')
ax2[0].set_ylabel('')
ax2[0].set_title('x histo')
#ax2[0].legend(loc='best')
#ax2[0].set_aspect('equal', 'box')


ax2[1].hist(y, 10, label='y')
ax2[1].set_xlabel('y')
ax2[1].set_ylabel('')
ax2[1].set_title('y histo')


ax2[2].hist(z, 10, label='z')
ax2[2].set_xlabel('z')
ax2[2].set_ylabel('')
ax2[2].set_title('z histo')

#fig2.show()
plt.show()