#!/usr/bin/env python3

# Python script which reads data from the files CO2.csv and temperature.csv
# and generates a labeled, nice plot of time vs. CO2 or time vs. temperature.
# Usage:
# python3 temperature_CO2_plotter.py

import sys
import re


def plot_temperature(months_to_plot=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], years, y_min, y_max):
    """Plots time vs temperature
        
        Args:
            months_to_plot (list): list containing months (1-12) to plot data from
            years (list): list containing yers to plot (eg. 1999, 2000, ...)
            y_min: Lowest y-axis value to plot
            y_max: highest y-axis value to plot

        Returns:
            None
        """


def plot_CO2(months_to_plot=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12], years, y_min, y_max):
    """Plots time vs CO2
        
        Args:
            months_to_plot (list): list containing months (1-12) to plot data from
            years (list): list containing yers to plot (eg. 1999, 2000, ...)
            y_min: Lowest y-axis value to plot
            y_max: highest y-axis value to plot

        Returns:
            None
        """

# Nice to have:
if __name__ == "__main__":
    # if len(sys.argv) < 2: # Print help
    #     print("python3 temperature_CO2_plotter.py")
    #     sys.exit("Commandline arguments error.")
    

