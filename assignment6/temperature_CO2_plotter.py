#!/usr/bin/env python3

# Python script which reads data from the files CO2.csv, temperature.csv and CO2_by_country.csv,
# then generates a labeled, nice plot of time vs. CO2, time vs. temperature, and CO2 emissions
# per capita for different countries.

# Usage:
# python3 temperature_CO2_plotter.py

import sys
import matplotlib.pyplot as plt

#The paths of the input files are specified here:
CO2_file="assignment6_files/co2.csv"
temperature_file="assignment6_files/temperature.csv"
CO2_by_contry_file="assignment6_files/CO2_by_country.csv"

def read_file(filepath, lines_end_with_comma=False):
    """Reads data from a file and stores it into two lists
        
        Args:
            filepath: String containing relative path (including filename) of the file you want to read
            lines_end_with_comma: One of the input files (that have lines ending with commas, needs special handling)

        Returns:
            header: List containing first line of the file (here interpreted as heading)
            data: A list that holds the rest of the data in the file
        """
    data = []
    with open(filepath) as file:
        for line in file:
            if lines_end_with_comma: #special handling
                line = line.strip().split("\",\"")
                for i in range(len(line)):
                    s=line[i]
                    if s.startswith('"'):
                        s = s[1:]
                    if s.endswith('"'):
                       s = s[:-1]
                    if s.endswith('",'):
                        s = s[:-2]
                    if s.endswith(','):
                        s = s[:-1]
                    line[i]=s
                data.append(line)
            else:
                data.append(line.strip().split(",")) #normal (default) easy operation
    header=data.pop(0)
    return header, data

def parse_num(s):
    """Parses the input either as an int or float, None if not number
       A little messy, but it gets the job done

        Args:
            s: input number (usually given in string-format)

        Returns:
            number (int/float/None): the parsed integer or float, None if not number
        """
    if s == "" or s == None: return None
    if s.startswith('"'):
        s = s[1:]
    if s.endswith('"'):
        s = s[:-1]
    if s == "" or s == None: return None
    try:
        return int(s)
    except ValueError:
        return float(s)

def find_regression_coefficient(x, y):
    """Uses linear regression analysis to find the coefficient to use for predicting future temperatures
       Simple algorithm based on a formula that can be found on:
       https://en.wikipedia.org/wiki/Regression_analysis
        
        Args:
            x: the x values to use
            y: the y values to use

        Returns:
            number (float): calculated regression coefficient
        """
    """"""
    x_sum, y_sum = 0, 0
    for i in range(len(x)):
        x_sum = x_sum + x[i]
        y_sum = y_sum + y[i]
    x_avg = x_sum / len(x)
    y_avg = y_sum / len(y)
    numerator, denominator = 0, 0
    for i in range(len(x)):
        numerator = numerator + (x[i] - x_avg) * (y[i] - y_avg)
        denominator = denominator + (x[i] - x_avg)**2
    return 1.0 * numerator / denominator

def plot_temperature(ymin=None, ymax=None, startyear=None, endyear=None, months_to_plot=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], show_figure=False, savepath="temperature_plot.svg", years_to_predict=0):
    """Plots time vs temperature, presents image (and can present image if specified)
        
        Args:
            months_to_plot (list): list containing months (1-12) to plot data from
            startyear: The year to start plotting from (eg. 1900), uses xmin if unspecified
            endyear: The year to end plotting from (eg. 2000), uses xmax if unspecified
            ymin: Lowest y-axis value to plot
            ymax: highest y-axis value to plot
            show_figure: shows the figure if true (not just saves to file)
            years_to_predict: If non zero, will predict temperatures the given number of years into the future based on historical data.
            savepath: Can be set to specify path to save image to

        Returns:
            None
        """
    header, data = read_file(temperature_file)
    x, y = [], []
    for d in data:
        year=d.pop(0)
        for i in range(len(d)):
            if (i+1) in months_to_plot:
                x.append(parse_num(year))
                y.append(parse_num(d[i]))
    plt.close(0)
    plt.figure(0) # needed for parallelization
    plt.plot(x, y)
    plt.xlabel(header[0])
    plt.ylabel("temperature")
    plt.ylim(ymin, ymax)
    xmin= (x[0] if startyear == None and years_to_predict == 0 else startyear)
    xmax= (x[-1] if endyear == None and years_to_predict == 0 else endyear)
    plt.xlim(xmin, xmax)
    if years_to_predict > 0:
        # Here we make our prediction of the future. Assumptions:
        # * Base prediction on historical data from the 20 latest years.
        # * Assume linear growth.
        delta_y = find_regression_coefficient(x[(len(x)-20):len(x)], y[(len(y)-20):len(y)]) 
        xpred, ypred = [], []
        for i in range(years_to_predict+1):
            ypred.append(y[-1] + (i+1)*delta_y)
            xpred.append(x[-1] + (i+1))
        plt.plot(xpred, ypred)
    plt.savefig(savepath)
    if show_figure: plt.show()

def plot_CO2(ymin=None, ymax=None, startyear=None, endyear=None, show_figure=False, savepath="CO2_plot.svg"):
    """Plots time vs CO2, saves to file (and can present image if specified)
        
        Args:
            startyear: The year to start plotting from (eg. 1900), uses xmin if unspecified
            endyear: The year to end plotting from (eg. 2000), uses xmax if unspecified
            ymin: Lowest y-axis value to plot
            ymax: highest y-axis value to plot
            show_figure: shows the figure if true (not just saves to file)
            savepath: Can be set to specify path to save image to

        Returns:
            None
        """
    header, data = read_file(CO2_file)
    x, y = [], []
    for d in data:
        x.append(parse_num(d[0]))
        y.append(parse_num(d[1]))
    plt.close(1)
    plt.figure(1) # needed for parallelization
    plt.plot(x, y)
    plt.xlabel(header[0])
    plt.ylabel(header[1])
    plt.ylim(ymin, ymax)
    xmin= (x[0] if startyear == None else startyear)
    xmax= (x[-1] if endyear == None else endyear)
    plt.xlim(xmin, xmax)
    plt.savefig(savepath)
    if show_figure: plt.show()

def plot_CO2_by_country(threshold=1000, is_above_threshold=True, ymin=None, ymax=None, startyear=None, endyear=None, show_figure=False, savepath="CO2_by_country.svg"):
    """Plots countries emissions of metric tons of CO2 per capita
        
        Args:
            threshold: Generates a bar chart of CO2 emissions below/above this set threshold
            is_above_threshold: if true, plots countries above threshold, else plots countries below
            startyear: Beginning year to count emissions for
            endyear: End year to count emissions for
            ymin: Lowest y-axis value to plot
            ymax: highest y-axis value to plot
            show_figure: shows the figure if true (not just saves to file)
            savepath: Can be set to specify path to save image to

        Returns:
            None
        """
    header, data = read_file(CO2_by_contry_file, lines_end_with_comma=True)
    x, y = [], []
    x_labels = []
    year_list=header[4:]
    for i in range(len(year_list)): year_list[i] = parse_num(year_list[i])
    for line in data:
        line.pop(0) #Country name
        country_string = line.pop(0)
        line.pop(0) #Indicator name
        line.pop(0) #Indicator code
        emission_sum = 0
        for i in range(len(line)):
            emission = line[i]
            parsed = parse_num(emission)
            #make sure that we only add emissions for the specified years:
            if parsed != None and ((startyear==None and endyear==None) or (endyear==None and year_list[i] >= startyear) or (startyear==None and year_list[i] <= endyear) or (year_list[i] >= startyear and year_list[i] <= endyear)):
                emission_sum = emission_sum + parsed
        #check if above or below treshold
        if (is_above_threshold and emission_sum >= threshold) or (is_above_threshold == False and emission_sum <= threshold):
            y.append(emission_sum)
            x_labels.append(country_string)
    for num in range(len(y)): x.append(num)
    plt.close(2)
    plt.figure(2) # needed for parallelization
    plt.bar(x, y, align='center')
    plt.xticks(x, x_labels)
    plt.ylim(ymin, ymax)
    plt.savefig(savepath)
    if show_figure: plt.show()

if __name__ == "__main__":
    """Main, will by default make some images and save them to the static folder."""
    plot_CO2(savepath="static/CO2_by_country.svg")
    plot_temperature(months_to_plot=[12], savepath="static/temperature_plot.svg")
    plot_temperature(months_to_plot=[1], savepath="static/temperature_plot_with_prediction.svg", years_to_predict=100)
    plot_CO2_by_country(savepath="static/CO2_by_country.svg")
