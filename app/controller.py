'''
Created on 23 Aug 2017

@author: sats
'''
from flask import make_response, jsonify
import logging


logging.basicConfig()
log = logging.getLogger(__name__)

def login():
    try:
        return make_response(jsonify({'message':'successfully logged in'}))
    except Exception as e:
        log.error(e)
        return make_response(jsonify({'error':'Either email or password is invalid'}), 401)
