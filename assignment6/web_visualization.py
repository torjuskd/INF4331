#!/usr/bin/env python3

# Simple web application for presenting CO2 and temperature data.

# Usage:
# python3 web_visualization.py

import sys
from flask import Flask

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
    
app = Flask(__name__)

@app.route("/")
def hello():
    pagestring = "<p>Hello World!</p>" + " " + "<img src=\""+CO2_file+"\" alt=\"CO2 Concentration\">" + "<img src=\""+temperature_file+"\" alt=\"Atmospheric temperature\">"
    print(pagestring)
    return pagestring

if __name__ == "__main__":
    app.run(debug=True, port=5002)
    print("it runs")
