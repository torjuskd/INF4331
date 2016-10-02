#!/usr/bin/env python3
# Calculate and writes an image of the Mandelbrot set.

import apply 
#from  apply import apply_mandelbrot
from matplotlib import pyplot as plt
from numpy import arange, zeros, NaN
import seaborn
import time

def mandelbrot_calc(stepLimit, startX, endX, startY, endY):
    xaxis = arange(startX, endX, .002)
    yaxis = arange(startY,  endY, .002)
    values = zeros((len(yaxis), len(xaxis)))
    for yindex in range(len(yaxis)):
        for xindex in range(len(xaxis)):
            values[yindex,xindex] = apply.apply_mandelbrot(xaxis[xindex], yaxis[yindex], stepLimit)
    return (xaxis, yaxis, values)

def draw(X, Y, values):
    # prism is nice for its reapeating colors, but we need to color pixels in the mandelbrot set black so we have to modify it.
    modifiedPrism = plt.cm.prism
    modifiedPrism.set_bad(color='#000000', alpha=None)
    modifiedPrism.set_under(color='#000000', alpha=None)
    plt.imshow(values, cmap = modifiedPrism, vmin=.001, interpolation = 'none', extent = (X.min(), X.max(), Y.min(), Y.max()))
    plt.xlabel("Real(c)")
    plt.ylabel("Imaginary(c)")
    plt.savefig("mandelbrot_plot3.svg")
    #plt.show() #Don't show yet only save to file.

# The values of these can be changed at your will.
stepLimit = 100
magicNum = 1.68033989
xyOffset = -1

startY = -1.5
endY = 1.5
startX = startY * magicNum + xyOffset
endX = endY * magicNum + xyOffset

t1 = time.clock()
# Here we do the calculations and write the resulting image.
result = mandelbrot_calc(stepLimit, startX, endX, startY, endY)
t2 = time.clock()
print('{:.3f} sec'.format(t2-t1))
draw(X=result[0], Y=result[1], values=result[2])

