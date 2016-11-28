#!/usr/bin/env python3

# Simple web application for presenting CO2 and temperature data.

# Usage:
# python3 web_visualization.py
import temperature_CO2_plotter as plotter
import sys
from flask import Flask
from flask import render_template
from flask import request
import time

CO2_file="CO2_plot.svg"
temperature_file="temperature_plot.svg"
temperature_file_path="static/"+temperature_file
CO2_file_path="static/"+CO2_file
app = Flask(__name__)

@app.route("/")
def start():
    plotter.plot_temperature(startyear=1825, savepath="static/"+temperature_file)
    plotter.plot_CO2(startyear=1825, savepath="static/"+CO2_file)
    return render_template("index.html",temperature_file_path=temperature_file_path, CO2_file_path=CO2_file_path)

@app.route("/ParametersChanged", methods=['POST'])
def change():
    time_from = plotter.parse_num(request.form["time_from"])
    time_to = plotter.parse_num(request.form["time_to"])
    yaxis_min_CO2 = plotter.parse_num(request.form["yaxis_min_CO2"])
    yaxis_max_CO2 = plotter.parse_num(request.form["yaxis_max_CO2"])
    yaxis_min_temperature = plotter.parse_num(request.form["yaxis_min_temperature"])
    yaxis_max_temperature = plotter.parse_num(request.form["yaxis_max_temperature"])

    months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    selected_months = []
    for m in months:
        selected_months.append(plotter.parse_num(request.form.get(m, None)))
    print(selected_months)
    
    plotter.plot_temperature(startyear=time_from, endyear=time_to, ymin=yaxis_min_temperature, ymax=yaxis_max_temperature, months_to_plot=selected_months, savepath="static/"+temperature_file)
    plotter.plot_CO2(startyear=time_from, endyear=time_to, ymin=yaxis_min_CO2, ymax=yaxis_max_CO2, savepath="static/"+CO2_file)

    return render_template("index.html",temperature_file_path=temperature_file_path, CO2_file_path=CO2_file_path)

@app.after_request
def apply_caching(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    return response

if __name__ == "__main__":
    #app = Flask(static_folder='..')
    app.run(debug=True, port=5002)

