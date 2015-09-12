'''
Created on Sep 12, 2015

@author: Glory
'''
import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello'