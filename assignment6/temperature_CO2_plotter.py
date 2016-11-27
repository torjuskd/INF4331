#!/usr/bin/env python3

# Python script which reads data from the files CO2.csv and temperature.csv
# and generates a labeled, nice plot of time vs. CO2 or time vs. temperature.
# Usage:
# python3 temperature_CO2_plotter.py

import sys
import re
import matplotlib.pyplot as plt

#The paths of the input files are specified here:
CO2_file="assignment6_files/co2.csv"
temperature_file="assignment6_files/temperature.csv"
CO2_by_contry_file="assignment6_files/CO2_by_country.csv"

def read_file(filepath):
    """Reads data from a file and stores it into two lists
        
        Args:
            filepath: String containing relative path (including filename) of the file you want to read

        Returns:
            header: List containing first line of the file (here interpreted as heading)
            data: A list that holds the rest of the data in the file
        """
    data = []
    with open(filepath) as file:
        for line in file:
            data.append(line.strip().split(","))
    header=data.pop(0)
    return header, data

def parse_num(s):
    """Parses the input either as an int or float
        
        Args:
            s: input number (usually given in string-format)

        Returns:
            number (int/float): the parsed integer or float
        """
    try:
        return int(s)
    except ValueError:
        return float(s)

def plot_temperature(ymin=None, ymax=None, startyear=None, endyear=None, months_to_plot=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], show_figure=False):
    """Plots time vs temperature, presents image (and can present image if specified)
        
        Args:
            months_to_plot (list): list containing months (1-12) to plot data from
            startyear: The year to start plotting from (eg. 1900), uses xmin if unspecified
            endyear: The year to end plotting from (eg. 2000), uses xmax if unspecified
            ymin: Lowest y-axis value to plot
            ymax: highest y-axis value to plot
            show_figure: shows the figure if true (not just saves to file)

        Returns:
            None
        """
    header, data = read_file(temperature_file)
    x, y = [], []
    for d in data:
        year=d.pop(0)
        for i in range(len(d)):
            if i in months_to_plot:
                x.append(parse_num(year))
                y.append(parse_num(d[i]))
    plt.plot(x, y)
    plt.xlabel(header[0])
    plt.ylabel("temperature")
    plt.ylim(ymin, ymax)
    xmin= (x[0] if startyear == None else startyear)
    xmax= (x[-1] if endyear == None else endyear)
    plt.xlim(xmin, xmax)
    plt.savefig("temperature_plot.svg")
    if show_figure: plt.show()

def plot_CO2(ymin=None, ymax=None, startyear=None, endyear=None, show_figure=False):
    """Plots time vs CO2, saves to file (and can present image if specified)
        
        Args:
            startyear: The year to start plotting from (eg. 1900), uses xmin if unspecified
            endyear: The year to end plotting from (eg. 2000), uses xmax if unspecified
            ymin: Lowest y-axis value to plot
            ymax: highest y-axis value to plot
            show_figure: shows the figure if true (not just saves to file)

        Returns:
            None
        """
    header, data = read_file(CO2_file)
    x, y = [], []
    for d in data:
        x.append(parse_num(d[0]))
        y.append(parse_num(d[1]))
    plt.plot(x, y)
    plt.xlabel(header[0])
    plt.ylabel(header[1])
    plt.ylim(ymin, ymax)
    xmin= (x[0] if startyear == None else startyear)
    xmax= (x[-1] if endyear == None else endyear)
    plt.xlim(xmin, xmax)
    plt.savefig("CO2_plot.svg")
    if show_figure: plt.show()

# Nice to have:
if __name__ == "__main__":
    # if len(sys.argv) < 2: # Print help
    #     print("python3 temperature_CO2_plotter.py")
    #     sys.exit("Commandline arguments error.")
    #plot_CO2()
#    plot_CO2(startyear=1900, endyear=2000)
#    plot_temperature(months_to_plot=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
    plot_temperature(months_to_plot=[1], show_figure=True)
#    plot_temperature([1999, 2000, 2001, 2002, 2003], 0, 1000)
