import matplotlib.pyplot as plt
import numpy as np

sr = 9600
freq = 60
ts = 1.0/sr

anum = np.arange(0,0.1,ts)
bnum = np.arange(0,0.1,ts)
cnum = np.arange(0,0.1,ts)
a1 = np.sin(2*np.pi*freq*anum)
b1 = np.sin(2*np.pi*freq*bnum + 2/3*np.pi)
c1 = np.sin(2*np.pi*freq*cnum + 4/3*np.pi)

fig, ax = plt.subplots()
ax.plot(anum, a1)
fig, bx = plt.subplots()
ax.plot(bnum, b1)
fig, cx = plt.subplots()
ax.plot(cnum, c1)
plt.show()
