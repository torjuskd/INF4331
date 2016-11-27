#!/usr/bin/env python3

# Python script which reads data from the files CO2.csv and temperature.csv
# and generates a labeled, nice plot of time vs. CO2 or time vs. temperature.
# Usage:
# python3 temperature_CO2_plotter.py

import sys
import Flask

CO2_file="CO2_plot.svg"
temperature_file="temperature_plot.svg"

def display_temperature(ymin=None, ymax=None, startyear=None, endyear=None, months_to_plot=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], show_figure=False):
    """Plots time vs temperature, presents image and saves to file
        
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
    

def display_CO2(ymin=None, ymax=None, startyear=None, endyear=None, show_figure=False):
    """Plots time vs CO2, presents image and saves to file
        
        Args:
            startyear: The year to start plotting from (eg. 1900), uses xmin if unspecified
            endyear: The year to end plotting from (eg. 2000), uses xmax if unspecified
            ymin: Lowest y-axis value to plot
            ymax: highest y-axis value to plot
            show_figure: shows the figure if true (not just saves to file)

        Returns:
            None
        """
    

# Nice to have:
if __name__ == "__main__":
    # if len(sys.argv) < 2: # Print help
    #     print("python3 temperature_CO2_plotter.py")
    #     sys.exit("Commandline arguments error.")
    print("it runs")
