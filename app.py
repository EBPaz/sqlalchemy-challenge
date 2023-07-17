# Import the dependencies.
import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from Flask import Flask, jsonify


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
@app.route("/")
def home():
    print("Accessing the Home Screen")
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/precipitation"
        f"/api/v1.0/stations"
        f"/api/v1.0/tobs<br/>"
        f"/api/v1.0/<start>"
        f"/api/v1.0/<start>/<end>"
    )

@app.route("/api/v1.0/precipitation")
def precipitation():
    print("Accessing the Precipitation Screen")
    session = Session.engine
    # Query the last 12 months of precipitation
    all_precip = session.query(Measurement.date, Measurement.prcp).filter(Measurement.date >= '2016-08-23').all()



# # # Sort the dataframe by date
# sorted_one_year_df = one_year_df.sort_values(by = ['date']) 
# sorted_one_year_df = sorted_one_year_df.set_index('date')

# session.close()

#     # Convert the tuples lists into a regular list
# annual_list = list(np.ravel(annual))

# return jsonify(annual_list)


# _name__ == '__main__':
# app.run(debug=True)