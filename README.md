## Project Title 
SQLalchemy challenge - Module 10, July 2023

## About
This project uses SQLalchemy to assess climate data for a vacation to Hawaii. First climate data was analyzed from 9 different weather stations throughout the island of Hawaii. Then we narrowed in on the most active weather station and calculated rainfall (preciptiation) statistics as well as temperature statistics. Finally, we used this collection of data to create an API to be able to search the weather for specific variables or specific date ranges. 

## Table of Contents
Resources
- hawaii.sqlite (sqlite database for hawaii data)
- hawaii_measurements.csv (csv of rainfall measurements)
- hawaii_stations.csv (csv of weather stations)

app.py (API to access specific data)

climate_starter.ipynb (data analysis from the above Resources)

## Getting Started / Installation
To reproduce the climate_starter data analysis, you need the following imports:
%matplotlib inline
from matplotlib import style
style.use('fivethirtyeight')
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, inspect, func

To reproduce the appy.py API build, you need the following imports:
import numpy as np
import datetime as dt
from datetime import datetime
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

## Acknowledgements
Help with the syntax on the use of func.count, specifically to answer this question: Design a query to find the most active stations (i.e. which stations have the most rows? ) 
I followed Aizelmarie M (amagsino on GitHub) at https://github.com/amagsino/SQLAlchemy-Challenge.git

I also worked closely with Aleid van der Zel, fellow classmate, on dynamic API recalls.
