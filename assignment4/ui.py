#!/usr/bin/env python3
# Calculate and writes an image of the Mandelbrot set.

from matplotlib import pyplot as plt
#from numpy import arange, zeros, NaN
#import seaborn
import time
import sys

import mandelbrot_1 as m1
import mandelbrot_2 as m2
import mandelbrot_3 as m3
import mandelbrot_4_starter as m4

def draw(X, Y, values, filename):
    # prism is nice for its reapeating colors, but we need to color pixels in the mandelbrot set black so we have to modify it.
    modifiedcm = plt.cm.prism
    modifiedcm.set_bad(color='#000000', alpha=None)
    modifiedcm.set_under(color='#000000', alpha=None)
    plt.imshow(values, cmap = modifiedcm, vmin=.001, interpolation = 'none', extent = (X.min(), X.max(), Y.min(), Y.max()))
    plt.xlabel("Real(c)")
    plt.ylabel("Imaginary(c)")
    plt.savefig(filename)
    #plt.show() #Don't show yet only save to file.

def help():
    usage_string = """usage: ./ui.py [filename] [option]
    Default filename is "mandelbrot_plot.svg", options and arguments:
    -xstart    : The lowest x-coordinate to start drawing from
    -xend      : The highest x-coordinate that will be drawn
    -ystart    : The lowest x-coordinate to start drawing from
    -yend      : The highest x-coordinate that will be drawn
    -r         : Resulotion to draw in, lower numbers give higer resolution (default: .002)
    -i         : Implementation to use, a number from 1 to 4 (default: 3)
    -steps     : Number of times to run number through mandelbrot function before concluding its in the set"""
    print(usage_string)
    sys.exit()


# Default values.
stepLimit = 1000
magicNum = 1.68033989
xyOffset = -1

startY = -1.5
endY = 1.5
startX = startY * magicNum + xyOffset
endX = endY * magicNum + xyOffset

#new parameters
implementation = 4
resolution = .002
filename = "mandelbrot_plot.svg"


#Specify region to draw, reslolution to draw in, output image filename, specify implementation
arguments = sys.argv[1:]

if len(arguments) > 0 and arguments[0] == "--help": # print help
    help()

while len(arguments) > 0:
    arg1 = arguments[0].strip()
    arg2 = arguments[1].strip()
    
    if arg1 == "-xstart":
        startX = float(arg2)

    elif arg1 == "-xend":
        endX = float(arg2)
        
    elif arg1 == "-ystart":
        startY = float(arg2)
        
    elif arg1 == "-yend":
        endY = float(arg2)

    elif arg1 == "-r":
        resolution = float(arg2)

    elif arg1 == "-i":
        implementation = int(arg2)
        
    elif arg1 == "-steps":
        stepLimit = int(arg2)

    else: #interpret as filename
        filename = arg1
        del arguments[0]
        continue

    del arguments[0]
    del arguments[0]



t1 = time.clock()
# Here we do the calculations and write the resulting image.
result = None
if implementation == 1:
    result = m1.mandelbrot_calc(stepLimit, startX, endX, startY, endY, resolution)
elif implementation == 2:
    result = m2.mandelbrot_calc(stepLimit, startX, endX, startY, endY, resolution)
elif implementation == 3:
    result = m3.mandelbrot_calc(stepLimit, startX, endX, startY, endY, resolution)
elif implementation == 4:
    result = m4.mandelbrot_calc(stepLimit, startX, endX, startY, endY, resolution)
else:
    result = m3.mandelbrot_calc(stepLimit, startX, endX, startY, endY, resolution)

t2 = time.clock()
print('{:.3f} sec'.format(t2-t1))
draw(X=result[0], Y=result[1], values=result[2], filename=filename)

