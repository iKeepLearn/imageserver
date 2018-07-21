#!/bin/env python
# -*- coding:utf-8 -*-

from flask import Flask,render_template
from .forms import login_form
from .config import Config
from flask_login import current_user,login_user
from flask_login import login_required


app = Flask(__name__)
app.config.from_object(Config)
login =  LoginManager(app)
login.login_view = 'index'

@app.route('/',method=['GET','POST'])
def index():
    if current_user.is_authenticated:
        return redirect(url_for('admin'))
    form = login_form()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password')
            return redirect(url_for('index'))
        login_user(user,)
        return redirect(url_for('index'))
    return render_template("index.html",form=form)

