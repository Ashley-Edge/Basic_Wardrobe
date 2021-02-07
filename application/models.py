#!/usr/bin/python3
#               models.py

##########  Imports ##########

from application import db
# from flask_login import UserMixin

##########  Person table    ##########

#class Person(db.Model):
#    id = db.Column(db.Integer, primary_key=True)
#    name = db.Column(db.String(30), nullable=False)
#    email = db.Column(db.String(30), nullable=False)
#    password = db.Coulmn(db.String(50), nullable=False)
#    wardrobe = db.relationship('Clothing', backref='person')

##########  Clothing table  ##########

class Clothing(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(200), nullable=False)
#    category = db.Column(db.String(20), nullable=False)
#    description = db.Column(db.String(20), nullable=False)

#   person_id = db.Column(db.String(20), db.ForeignKey('person.id'), nullable=False)

    def __rep__(self):
        return '<Item %r>' % self.id

##########  

