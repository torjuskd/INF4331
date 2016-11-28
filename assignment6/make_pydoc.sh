#!/bin/bash
#Simple command for generating pydoc of the file temperature_CO_plotter.py

pydoc3 -w ./temperature_CO2_plotter.py
mv temperature_CO2_plotter.html ./templates
echo "pydoc generated and put in /templates."
