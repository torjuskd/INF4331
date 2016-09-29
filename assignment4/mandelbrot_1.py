#!/usr/bin/env python3

# from numpy import *
# from matplotlib import pyplot


from matplotlib import pyplot
from numpy import linspace, cos, exp, pi, random, arctan2, array, empty
#import seaborn       

countLimit = 100
count = 0
x0 = 0
c = -1
z = 0



def mandelbrot(c, z, steps):
    #find out if mandelbrot - black
    #return -1 if yes, else how many steps (color according to amount of steps)
    if abs(z) > 2:
        return steps
    if steps < countLimit:
        z = z * z + c
        mandelbrot(c, z, steps + 1)
    else:
#        return -1
        return 0

def mandelbrot_calc():
    start = -1
    end = 1
    rectangleheight = 1000
#    rectanglewidth = int(rectangleheight * 1.68033989)
    rectanglewidth = 1000
    xaxis = linspace(start, end, rectanglewidth)
    yaxis = linspace(start, end, rectangleheight)
    values = empty((rectanglewidth, rectangleheight))
    for i in range(rectanglewidth):
        for j in range(rectangleheight):
            values[i, j] = mandelbrot(xaxis[i] + 1j*yaxis[j], 0, 0)
    return (xaxis, yaxis, values)

result = mandelbrot_calc()



test = int(abs(result[2]) > 2)

n = 1024
X = result[0]
Y = result[1]
T = test

#pyplot.axes([0.025, 0.025, 0.95, 0.95])
pyplot.scatter(X, Y, s=75, c=T, alpha=.5)


pyplot.show()











# n = 2000
# x = linspace(-1.0, 1.0, n, endpoint=True) # coordinates    
# rectangle = array([x, x])

# figure = pyplot.figure()
# ax = figure.add_subplot(1, 1, 1)

# #x = rectangle[:,0]
# y = rectangle[:,1]


# #pyplot.axes([0.025, 0.025, 0.95, 0.95]) 
# pyplot.scatter(x, x, s=75, alpha=.5)


# pyplot.show()





# n = 1024
# X = random.normal(0, 1, n)
# Y = random.normal(0, 1, n)
# T = arctan2(Y, X)

# pyplot.axes([0.025, 0.025, 0.95, 0.95])
# pyplot.scatter(X, Y, s=75, c=T, alpha=.5)


# pyplot.show()
