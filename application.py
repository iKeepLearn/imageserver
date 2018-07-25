#!/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask,render_template,request,redirect,url_for,session
from .forms import login_form
from .config import Config


app = Flask(__name__)
app.config.from_object(Config)

ADMIN_USERNAME = Config.ADMIN_USERNAME
ADMIN_PASSWORD = Config.ADMIN_PASSWORD

from .admin.admin import admin
app.register_blueprint(admin,url_prefix='/admin')



@app.route('/')
def index():
    form = login_form()
    return render_template('index.html',form=form)

@app.route('/login',methods=['GET','POST'])
def login():
    form = login_form()
    if request.form['password'] == ADMIN_PASSWORD and request.form['username'] ==ADMIN_USERNAME:
        session['logged_in'] = True
        return redirect(url_for('admin.admin_page'))
    else:
        return render_template('index.html',form=form)
