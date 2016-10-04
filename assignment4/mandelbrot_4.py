#!/usr/bin/env python3
# Calculate and writes an image of the Mandelbrot set.

# set up with:
# swig -python mandelbrot_4_swig.i
# python3 mandelbrot_4_setup.py build_ext --inplace

import mandelbrot_4_swig
from matplotlib import pyplot as plt
from numpy import arange, zeros, NaN
#import seaborn
import time

def mandelbrot_calc(stepLimit, startX, endX, startY, endY, resolution):
    xaxis = arange(startX, endX, resolution)
    yaxis = arange(startY,  endY, resolution)
    values = zeros((len(yaxis), len(xaxis)))
    for yindex in range(len(yaxis)):
        for xindex in range(len(xaxis)):
            values[yindex,xindex] = mandelbrot_4_swig.mandelbrot_4(xaxis[xindex], yaxis[yindex], stepLimit)
    return (xaxis, yaxis, values)

def draw(X, Y, values):
    # prism is nice for its reapeating colors, but we need to color pixels in the mandelbrot set black so we have to modify it.
    modifiedPrism = plt.cm.prism
    modifiedPrism.set_bad(color='#000000', alpha=None)
    modifiedPrism.set_under(color='#000000', alpha=None)
    plt.imshow(values, cmap = modifiedPrism, vmin=.001, interpolation = 'none', extent = (X.min(), X.max(), Y.min(), Y.max()))
    plt.xlabel("Real(c)")
    plt.ylabel("Imaginary(c)")
    plt.savefig("mandelbrot_plot4.svg")
    #plt.show() #Don't show yet only save to file.

if __name__ == "__main__":
    # The values of these can be changed at your will.
    resolution = .002
    stepLimit = 100
    magicNum = 1.68033989
    xyOffset = -1
    startY = -1.5
    endY = 1.5
    startX = startY * magicNum + xyOffset
    endX = endY * magicNum + xyOffset
    t1 = time.clock()
    # Here we do the calculations and write the resulting image.
    result = mandelbrot_calc(stepLimit, startX, endX, startY, endY, resolution)
    t2 = time.clock()
    print('{:.3f} sec'.format(t2-t1))
    draw(X=result[0], Y=result[1], values=result[2])
