from  pylab import *
x = arange(0,100)
y = x**2
fig1 = figure()
ax = fig1.add_subplot(111)
ax.plot(x,y)
savefig('figure.png')
