##auth logout implementation
from flask import Flask, request
from json import dumps
import jwt

from data import *
from token_check import token_check
'''
Given an active token, invalidates the taken to log the user out. Given a non-valid token, does nothing

N/A
'''

# @APP.route('/auth/logout', methods=['POST'])
def auth_logout():

    # create the dictionary
    ret
    # if the token is a valid token, delete the token and return true
    # otherwise, return false

    token = request.form.get('token')

    global data
    data = getData()

    global SECRET
    SECRET = getSecret()

    if token_check(token):
        for key, users in data['users'].items():
            if users['u_id'] == jwt.decode(token, SECRET, algorithm='HS256'):
                # user is a valid user
                users['logginin'] = False
                ret = True
                return dumps(ret)
                
    else:
        ret = False
        return dumps(ret)   


