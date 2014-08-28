MarkovBaseball-webapp
=====================

<center><img src ="http://cl.ly/XGLw/download/Screen%20Shot%202014-08-27%20at%2011.57.27%20PM.png" height="500" /></center>


Overview
=====================
This is an application designed to demonstrate the application of markov chains to baseball. The site parses the CCCBA or the California Community College Baseball league Statistics page nightly, using a python library called Scrapy. A cron job is set up to run nightly to grab the most recent data to display on the site.

The webapp is built using Django. The webserver is gunicorn with nginx to serve the static assets. 

All of the graphs on the home page were created using the D3 javascript library, and all the graphs for the team pages were created using the chart.js library.



How to Run
=====================

Scrapy
--------------
All of the scrapy files are located in the directory [markov_baseball](https://github.com/vsharm/markovbaseball-webapp/tree/master/markov_baseball). 

To run scrapy cd into [markov_baseball](https://github.com/vsharm/markovbaseball-webapp/tree/master/markov_baseball) and run ```scrapy crawl ccba -o ccba.json -t json```. To sort that data run ```python sort.py```.

Django
--------------
All of the Django Files are located in the directory [markovbaseball](https://github.com/vsharm/markovbaseball-webapp/tree/master/markovbaseball). 

To run the Django development server cd into [markovbaseball](https://github.com/vsharm/markovbaseball-webapp/tree/master/markovbaseball) and run ```python manage.py runserver 0.0.0.0:[port#]```

Math
--------------
The two main mathematical files are 
