'''
Created on 23 Aug 2017

@author: sats
'''
'''
a common method for loading a File 
'''

from flask import Flask
import json
import logging
from logging.config import dictConfig
import os

''' load flask app'''

app = Flask(__name__)
app.config.from_object(__name__)

def load_file(file_name):
    full_path = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), "."))
    file_path = file_name % os.path.dirname(full_path)
    return file_path

api = json.load(open(load_file('%s/config/api_uri.json'), 'r'))