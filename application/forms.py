#!/usr/bin/python3

#               forms.py

##########  imports   ##########

from flask_wtf import FlaskForm
from wtforms import TextField, StringField, SubmitField, HiddenField, SelectField, FloatField
from wtforms.validators import DataRequired, Length, ValidationError, Email
#from app import db
from application.models import *
