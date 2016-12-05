- Assignment6: Web
  * temperature_CO2_plotter.py (module that draws graphs, and saves them as picures)
    - documentation can be found on the webpage (or in templates/temperature_CO2_plotter.html)
      - a simple script (make_pydoc.sh) can be used to generate this pydoc
    - draws graphs based on input files in /assignment6_files
    - run with "python3 temperature_CO2_plotter.py"
  * web_visualization.py (Webpage that presents graphs made with the plotter)
    - uses html templates from /templates and images from /static
    - run with "python3 web_visualization.py"
  * make_pydoc.sh - simple script to generate pydoc and put it in templates folder
  * ./templates - folder holding html files.
  * ./static - folder for images, div files.