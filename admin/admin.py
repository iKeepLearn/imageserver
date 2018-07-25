#!/bin/env python
# -*- coding:utf-8 -*-

from flask import Blueprint,render_template,redirect,url_for,session


admin = Blueprint('admin',__name__,template_folder='templates',static_folder='static')


@admin.route('/')
def admin_page():
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    else:
        return render_template('admin.html',)

@admin.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('index'))
