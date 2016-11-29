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
CO2_by_country_filepath="static/CO2_by_country.svg"
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
    years_to_predict = plotter.parse_num(request.form["years_to_predict"])

    months = ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"]
    selected_months = []
    for m in months:
        selected_months.append(plotter.parse_num(request.form.get(m, None)))
        
    plotter.plot_temperature(startyear=time_from, endyear=time_to, ymin=yaxis_min_temperature, ymax=yaxis_max_temperature, months_to_plot=selected_months, savepath="static/"+temperature_file, years_to_predict=years_to_predict)
    plotter.plot_CO2(startyear=time_from, endyear=time_to, ymin=yaxis_min_CO2, ymax=yaxis_max_CO2, savepath="static/"+CO2_file)

    return render_template("index.html",temperature_file_path=temperature_file_path, CO2_file_path=CO2_file_path)

@app.route("/CO2_by_country")
def CO2_by_country():
    plotter.plot_CO2_by_country(savepath="static/CO2_by_country.svg")
    return render_template("CO2_by_country.html", CO2_by_country_filepath=CO2_by_country_filepath)

@app.route("/CO2_by_country_updated", methods=['POST'])
def CO2_by_country_changed():
    is_above_threshold = (True if plotter.parse_num(request.form["is_above_threshold"]) == 1 else False)
    threshold = plotter.parse_num(request.form["threshold"])
    if threshold == None: treshold=1000
    plotter.plot_CO2_by_country(threshold=threshold, is_above_threshold=is_above_threshold, savepath="static/CO2_by_country.svg")
    return render_template("CO2_by_country.html", CO2_by_country_filepath=CO2_by_country_filepath)

@app.route("/help")
def help():
    return render_template("temperature_CO2_plotter.html")

@app.after_request
def apply_caching(response):
    response.headers['Cache-Control'] = 'no-cache, no-store, must-revalidate'
    response.headers['Pragma'] = 'no-cache'
    return response

if __name__ == "__main__":
    app.run(debug=True, port=5002)

