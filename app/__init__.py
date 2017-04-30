from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_heroku import Heroku
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:pro2@localhost/pro2'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgresql://vshoylfhfcxyjh:7f0a971f015d8ed8d23c9f1bbeb2c9d50f36a77c1aa39f92bbdf5bc9bdd37565@ec2-54-235-72-121.compute-1.amazonaws.com:5432/d36q9igatgd33'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
db = SQLAlchemy(app)
heroku = Heroku(app)

db.create_all()
from app import views, models

