#!/usr/bin/python3
#               routes.py file

##########  Imports ##########

from flask import render_template, request, redirect, url_for
from application import app, db
#from application import bdrypt, login_manager
from application.forms import *
from application.models import *
#from flask_login import login_required, current_user, login_user

##########   Create   ##########

@app.route('/', methods=['POST', 'GET'])
def home():
    if request.method == 'POST':
        item_name = request.form['name']
        new_item = Clothing(name=item_name)

        try:
            db.session.add(new_item)
            db.session.commit()
            return redirect('/')
        except:
            return 'There was an error while adding the item'
    else:
        items = Clothing.query.all()
        return render_template("index.html", items=items)

##########   Delete  ##########

@app.route('/delete/<int:id>')
def delete(id):
    item_to_delete = Clothing.query.get_or_404(id)
    try:
        db.session.delete(item_to_delete)
        db.session.commit()
        return redirect('/')
    except:
        return 'Sorry, there was an error while deleting that item'

##########   Update  ##########

@app.route('/update/<int:id>', methods=['GET','POST'])
def update(id):
    item = Clothing.query.get_or_404(id)
    if request.method == 'POST':
        item.name = request.form['name']
        try:
            db.session.commit()
            return redirect('/')
        except:
            return 'Sorry, there was an issue while updating that item. Please go back and try again'
    else:
        return render_template('update.html', item=item)

