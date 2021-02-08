#!/usr/bin/python3

#               forms.py

##########  imports   ##########

from flask_wtf import FlaskForm
from wtforms import TextField, StringField, SubmitField, HiddenField, SelectField, FloatField
from wtforms.validators import DataRequired, Length, ValidationError, Email
#from app import db
from application.models import *

##########  New user    ##########

type_of_clothing =['top', 'botton', 'dress']

class NewClothing(FlaskForm):
    clothing_id = HiddenField('id')
    name = StringField('name', validators =[Length(min=2, max=200)])
#    category = SelectField('category', choices=[(typ, typ) for typ in type_of_clothing])
#    description = TextField('description', validators=[Length(min=2, max=500)])


