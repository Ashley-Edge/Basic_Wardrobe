#!/usr/bin/python3

##########  __init__.py  ##########

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
#from flask_bcrypt import Bcrypt
#from flask_login import LoginManager

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://ashley:penelo@localhost/test_db'
#app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///flask_db'
app.config['SECRET_KEY'] = 'penelopig'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

from application import routes
