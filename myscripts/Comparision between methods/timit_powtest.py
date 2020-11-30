import timeit
import matplotlib.pyplot as plt

t1=[]
t2=[]
dt=[]
dtt=[]
x,y,z=0,100000,10000
for i in range(x,y,z):
    dtt=[]
    for j in range(x,y,z):
        t1.append(timeit.timeit('powtest.p1(i,j)', setup='import powtest',number=10,globals=globals()))
        t2.append(timeit.timeit('powtest.p2(i,j)', setup='import powtest',number=10,globals=globals()))
        dtt.append(abs(t2[-1]-t1[-1]))
    dt.append(dtt)
r1=[i for i in range(x,y,z)]
r2=[j for j in range(x,y,z)]

fig,ax=plt.subplots()
for i in range(len(r1)):
    ax.plot(r2,dt[i],label=r1[i])
ax.set_xlabel('x label')  # Add an x-label to the axes.
ax.set_ylabel('y label')  # Add a y-label to the axes.
ax.set_title("Simple Plot")  # Add a title to the axes.
ax.legend()
plt.show()

