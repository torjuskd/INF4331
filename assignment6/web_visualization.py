#!/usr/bin/env python3

# Simple web application for presenting CO2 and temperature data.

# Usage:
# python3 web_visualization.py
import temperature_CO2_plotter as plotter
import sys
from flask import Flask
from flask import render_template
from flask import request

CO2_file="CO2_plot.svg"
temperature_file="temperature_plot.svg"
app = Flask(__name__)

@app.route("/")
def hello():
    plotter.plot_temperature(startyear=1825, savepath="static/"+temperature_file)
    plotter.plot_CO2(startyear=1825, savepath="static/"+CO2_file)
    return render_template("index.html")

if __name__ == "__main__":
    #app = Flask(static_folder='..')
    app.run(debug=True, port=5002)

