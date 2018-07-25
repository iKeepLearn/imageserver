#! -*- coding:utf-8 -*-

import os 
class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'fuck you what are you doing'
    ADMIN_USERNAME = 'dd'
    ADMIN_PASSWORD = 'dd'
