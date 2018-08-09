#!/bin/env python
# -*- coding:utf-8 -*-

from flask import Blueprint,render_template,redirect,url_for,session
from .forms import *

admin = Blueprint('admin',__name__,template_folder='templates',static_folder='static')


@admin.route('/')
@admin.route('/dashboard')
def admin_page():
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    else:
        return render_template('admin.html',)

@admin.route('/logout')
def logout():
    session['logged_in'] = False
    return redirect(url_for('index'))

@admin.route('/download')
def download():
    form = download_form()
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    else:
        return render_template('download.html',form=form)

@admin.route('/rmrepeat')
def rmrepeat():
    form = download_form()
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    else:
        return render_template('rmrepeat.html',form=form)

@admin.route('/split')
def split():
    form = download_form()
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    else:
        return render_template('split.html',form=form)

@admin.route('/convert')
def convert():
    form = download_form()
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    else:
        return render_template('convert.html',form=form)

@admin.route('/generation')
def generation():
    form = download_form()
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    else:
        return render_template('generation.html',form=form)

@admin.route('/view')
def view():
    form = download_form()
    if not session.get('logged_in'):
        return redirect(url_for('index'))
    else:
        return render_template('view.html',form=form)
