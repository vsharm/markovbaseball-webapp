MarkovBaseball-webapp
=====================
![alt tag](http://cl.ly/XGLw/download/Screen%20Shot%202014-08-27%20at%2011.57.27%20PM.png)

Overview
=====================
This is an application designed to demonstrate the application of markov chains to baseball. The site parses the CCCBA or the California Community College Baseball league Statistics page nightly, using a python library called Scrapy. A cron job is set up to run nightly to grab the most recent data to display on the site.

The webapp is built using Django. The webserver is gunicorn with nginx to serve the static assets. 

All of the graphs on the home page were created using the D3 javascript library, and all the graphs for the team pages were created using the chart.js library.
