# Import the dependencies.
import numpy as np
import datetime as dt
from datetime import datetime
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
Base = automap_base()

# reflect the tables
Base.prepare(autoload_with=engine)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station

# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
#################################################
app = Flask (__name__)

#################################################
# Flask Routes
#################################################
"""List the available API routes."""

#create a home route for all of the routes
@app.route("/")
def home():
    print("accessing the home screen")
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation<br/>"
        f"/api/v1.0/stations<br/>"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start><br/>"
        f"/api/v1.0/<start>/<end>"
    )

#create a route for the precipitation data
@app.route("/api/v1.0/precipitation")
def precipitation():
    print("accessing the precipitation screen")
    session = Session(engine)
    
    # Query the last year of precipitation data
    all_precip = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= '2016-08-23').all()

    session.close()

    precip_results = list(np.ravel(all_precip))
    
    return jsonify(precip_results)

#create a route for the station data
@app.route("/api/v1.0/stations")
def stations():
    print("accessing the stations screen")
    session = Session(engine)

    # Query for a list of stations
    list_of_stations = session.query(Station.name).all()
    
    session.close()

    # change the data to the right array
    all_stations = list(np.ravel(list_of_stations))

    return jsonify(all_stations)

#create a route for the temperature data
@app.route("/api/v1.0/tobs")
def tobs():
    print("accessing the observed temperatures screen")
    session = Session(engine)

    #Query to find the temperatures at the most-active stations for the last year
    active_station_annual = session.query(Measurement.tobs).filter(Measurement.station == "USC00519281")\
    .filter(Measurement.date >= '2016-08-23').all()

    session.close()

    #change the data to the right array
    annual_temperature = list(np.ravel(active_station_annual))

    return jsonify(annual_temperature)

#create a route for summary temperature data starting with a specific date
@app.route("/api/v1.0/<start>")
def start(start):
    print("accessing the summary data with a start date screen")
    session = Session(engine)

    start == datetime.strptime(start,'%Y-%m-%d').date()

    #query for min, max and average temperatures based on date input
    calculations = [func.min(Measurement.tobs),
                    func.max(Measurement.tobs),
                    func.avg(Measurement.tobs)]
    most_active_station_totals = session.query(*calculations).filter(Measurement.date >= start)\
    .order_by(Measurement.date).all()

    session.close()

    start_date_stats = list(np.ravel(most_active_station_totals))
    
    return jsonify(start_date_stats)

@app.route("/api/v1.0/<start>/<end>")
def summary2(start_end):
    print("accessing the summary data for a start and end date screen")
    session = Session(engine)

    start_end == datetime.strptime(start_end,'%Y-%m-%d').date()

    #query for min, max and average temperatures based on date input    
    calculations = [func.min(Measurement.tobs),
                    func.max(Measurement.tobs),
                    func.avg(Measurement.tobs)]
    most_active_station_totals = session.query(*calculations).filter(Measurement.date >= start_end).all()

    session.close()

    start_date_stats = list(np.ravel(most_active_station_totals))
    
    return jsonify(start_date_stats)

if __name__ == '__main__':
    app.run(debug=True)