#https://gist.github.com/glarrain/32c48ec01437f7c22d84586eca10443b


import sqlalchemy
import os
import logging
import numpy as np
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import pandas as pd

from flask import Flask, jsonify,render_template

#################################################
# Flask Setup
#################################################
app = Flask(__name__)

#DATABASE_URL: postgres://azrqiefezenfrg:Zti5fjSyeyFgoc-U-yXnPrXHQv@ec2-54-225-151-64.compute-1.amazonaws.com:5432/d2kio2ubc804p7

#################################################
# Database Setup
#################################################

v_database="project4"
v_user="postgres"
v_password="wVxBXGrDQ5JhHcA"
v_host="bootcampproject4.ceqr0hcm5qlq.us-east-1.rds.amazonaws.com"
v_port='5432'

from flask_sqlalchemy import SQLAlchemy
#app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', '') or "sqlite:///db.sqlite"

dburl= "postgresql://"+v_user+":"+v_password+"@"+v_host+":"+v_port+"/"+v_database

app.config['SQLALCHEMY_DATABASE_URI'] = dburl

# Remove tracking modifications
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

@app.route("/")
def home():

    print("aaaa")
    print("DB URL ", dburl)
    return render_template("index.html")  



from models import telecom_customer_churn as tcc
from models import telecom_zipcode_population as tzp



@app.route("/api/v0/telecom_zipcode_population")
def telecom_zipcode_population():

    l_list = []
    l_dict = {}

    results = db.session.query(tzp.population, tzp.zipcode).all()
   
    
    for i in range(len(results)):
        
        
        l_dict = {
                "zipcode": results[i][1],
                "population": results[i][0]
           }

        l_list.append(l_dict)

    return jsonify(l_list)  


if __name__ == '__main__':
    app.run(debug=True)