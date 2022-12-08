from flask import Flask, jsonify
import pandas as pd
from sqlHelper_vm import SQLHelper

#################################################
# Flask Setup
#################################################
app = Flask(__name__)
sqlHelper = SQLHelper()

#################################################
# Flask Routes
#################################################
@app.route("/")
def welcome():
    return (
        f"""Welcome to the Hawaii Weather API <br>
        <a href='/api/v1.0/precipitation'>/api/v1.0/precipitation</a> <br>
        <a href='/api/v1.0/stations'>/api/v1.0/stations</a> <br>
        <a href='/api/v1.0/tobs'>/api/v1.0/tobs</a> <br>"""
    )

@app.route("/api/v1.0/precipitation")
def get_precip():
    df = sqlHelper.getprecip()
    data = df.to_dict(orient="records")
    return(jsonify(data))

@app.route("/api/v1.0/stations")
def get_stations():
    df = sqlHelper.getstations()
    data = df.to_dict(orient="records")
    return(jsonify(data))

@app.route("/api/v1.0/tobs")
def get_tobs():
    df = sqlHelper.gettobs()
    data = df.to_dict(orient="records")
    return(jsonify(data))

@app.route("/api/v1.0/<start>")
def get_start_temp_date(start):
    df = sqlHelper.getstarttempdate(start)
    data = df.to_dict(orient="records")
    return(jsonify(data))

@app.route("/api/v1.0/<start>/<end>")
def get_end_temp_date(start, end):
    df = sqlHelper.getendtempdate(start, end)
    data = df.to_dict(orient="records")
    return(jsonify(data))
    
    
if __name__ == "__main__":
    app.run(debug=True)
