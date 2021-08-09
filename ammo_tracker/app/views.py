# pylint: disable=no-member
from app import app
from flask import render_template, request, jsonify, redirect, send_from_directory
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import json
from flask_wtf import FlaskForm 
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm 
from flask_bootstrap import Bootstrap
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from werkzeug.security import generate_password_hash, check_password_hash

import os

import pandas as pd
import sqlite3

bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

dbpath = '/Users/zach/Documents/Coding/ammo_tracker/database.db'


app.config['SECRET_KEY'] = 'Thisissupposedtobesecret!'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////Users/zach/Documents/Coding/ammo_tracker/database.db'


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    caliber = db.Column(db.String(15))
    count = db.Column(db.Integer)
    

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/', methods=['POST', 'GET'])
def index():
    # with sqlite3.connect(dbpath) as con:
    #     new_user = User(caliber=caliber, count=0)        
    #     db.session.add(new_user)
    #     db.session.commit()
            
    return render_template('index.html')


@app.route('/remove-db', methods=['GET', 'POST'])
def removeDB():
    data = request.get_json()
    dataArray = []
    for keys in data:
        dataArray.append(data[keys])
    caliber = dataArray[0]
    amount = dataArray[1]
    print(caliber, amount)

    with sqlite3.connect(dbpath) as con:
        c = con.cursor()
        c.execute('SELECT count FROM user WHERE caliber = ?', ([caliber]))
        res = c.fetchall()
        res = str(res)
        res = res.replace('[(', '')
        res = res.replace(',)]', '')
        print('-'*200)
        print(res)
        res = int(res)
        c.execute('UPDATE user SET count = ? WHERE caliber = ?', (res-amount, caliber))
        rv = c.fetchall()
        print(rv)
    return redirect("/pullData")



@app.route('/add-db', methods=['GET', 'POST'])
def addDB():
    data = request.get_json()
    dataArray = []
    for keys in data:
        dataArray.append(data[keys])
    caliber = dataArray[0]
    amount = dataArray[1]
    print(caliber, amount)

    with sqlite3.connect(dbpath) as con:
        c = con.cursor()
        c.execute('SELECT count FROM user WHERE caliber = ?', ([caliber]))
        res = c.fetchall()
        res = str(res)
        res = res.replace('[(', '')
        res = res.replace(',)]', '')
        print('-'*200)
        print(res)
        res = int(res)
        c.execute('UPDATE user SET count = ? WHERE caliber = ?', (amount+res, caliber))
        rv = c.fetchall()
        print(rv)
    return redirect("/pullData")



@app.route('/pullData', methods=['POST', 'GET'])
def pullData():
    json_data = []
    with sqlite3.connect(dbpath) as con:
        c = con.cursor()
        c2 = con.cursor()
        c.execute('SELECT * FROM user')
        rv = c.fetchall()
        json_data.append(rv)
        json_data = str(json_data)
        json_data = json_data.replace("[[('", "")
        json_data = json_data.replace("',)]]", "")
        print(rv)
        print(json_data)

    return jsonify(rv)


@app.route('/addCaliber', methods=['POST', 'GET'])
def addCaliber():
    caliber = request.get_json()
    with sqlite3.connect(dbpath) as con:
        new_user = User(caliber=caliber, count=0)    
        db.session.add(new_user)
        db.session.commit()
            
    return ('success')