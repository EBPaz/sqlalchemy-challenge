# Import the dependencies.
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify


#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurements
Station = Base.classes.stations

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask (__Climate_App__)

#################################################
# Flask Routes
#################################################
"""List the available API routes."""

#create a home route for all of the routes
@app.route("/")
def home():
    print("Accessing the Home Data")
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
    )

#create a route for the precipitation data
@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Accessing the Precipitation Data")
    session = Session.engine
    
    # Query the last year of precipitation data
    all_precip = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= '2016-08-23').all()

    session.close()
    
    #turn data into a set of dictionaries
    annual_list = []
    for date, prcp in results:
        annual_precip_dict = {}
        annual_precip_dict["date"] = date
        annual_precip_dict["prcp"] = prcp
        annual_list.append(annual_precip_dict)
    
    return jsonify(annual_list)

#create a route for the station data
@app.route("/api/v1.0/stations")
def stations():
    print("Accessing the Stations Data")
    session = Session(engine)

    # Query for a list of stations
    list_of_stations = session.query(station.name).all()

    session.close()

    # change the data to the right array
    all_stations = list(np.ravel(list_of_stations))

    return jsonify(all_stations)

#create a route for the temperature data
@app.route("/api/v1.0/temperature")
def temperature():
    print("Accessing the Temperature Data")
    session = Session.engine

    #Query to find th temperatures at the most-active stations for the last year
    active_station_annual = session.query(Measurement.tobs).filter(Measurement.station == "USC00519281")\
    .filter(Measurement.date >= '2016-08-23').all()

    session.close()

    #change the data to the right array
    annual_temperature = list(np.ravel(active_station_annual))

    return jsonify(annual_temperature)

#create a route for summary temperature data within specific dates
@app.route("/api/v1.0/<start>")
def summary1(start):
    print("accessing the summary data with a start date")
    session = Session.engine
    #query for min, max and average temperatures based on date input
    calculations = [func.min(Measurement.tobs),
                    func.max(Measurement.tobs),
                    func.avg(Measurement.tobs)]
    most_active_station_totals = session.query(*calculations).filter(Measurement.date >= start).all()

    session.close()

    #turn data into a dictionary response
    summary_data = []
    for calcs in most_active_station_totals:
        summary_temp = {}
        summary_temp["min"] = func.min(Measurement.tobs)
        summary_temp["max"] = func.min(Measurement.tobs)
        summary_temp["avc"] = func.min(Measurement.tobs)
        summary_data.append(summary_temp)
    
    return jsonify(summary_data)

@app.route("/api/v1.0/<start>/<end>")
def summary2(start_end):
    print("accessing the summary data for a start and end date")
    session = Session.engine
    #query for min, max and average temperatures based on date input    
    calculations = [func.min(Measurement.tobs),
                    func.max(Measurement.tobs),
                    func.avg(Measurement.tobs)]
    most_active_station_totals = session.query(*calculations).filter(Measurement.date >= start_end).all()

    session.close()

    #turn data into a dictionary response
    summary_data = []
    for calcs in most_active_station_totals:
        summary_temp = {}
        summary_temp["min"] = func.min(Measurement.tobs)
        summary_temp["max"] = func.min(Measurement.tobs)
        summary_temp["avc"] = func.min(Measurement.tobs)
        summary_data.append(summary_temp)
    
    return jsonify(summary_data)

if _name__ == '__main__':
    app.run(debug=True)