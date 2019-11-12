##auth logout implementation
from flask import Flask, request, Blueprint
from json import dumps
import jwt

from data import *
from token_check import token_check
'''
Given an active token, invalidates the taken to log the user out. Given a non-valid token, does nothing

N/A
'''

def auth_logout(token):

    # create the dictionary
    # if the token is a valid token, delete the token and return true
    # otherwise, return false

    global data
    data = getData()

    global SECRET
    SECRET = getSecret()

    if token_check(token):
        for key, users in data['users'].items():
            if {'u_id': users['u_id']} == jwt.decode(token, SECRET, algorithm='HS256'):
                # user is a valid user
                users['loggedin'] = False
                ret = True
                return ret
                
    else:
        ret = False
        return ret   




logout = Blueprint('APP_logout', __name__)
@logout.route('/auth/logout', methods=['POST'])
def Logout():

    # create the dictionary
    # if the token is a valid token, delete the token and return true
    # otherwise, return false

    token = request.form.get('token')
    return dumps( auth_logout(token)  )