from json import dumps
from flask import request, Blueprint
import jwt
from data import *
from email_check.py import *
from token_check import *

SETMAIL = Blueprint('SETMAIL', __name__)

@SETMAIL.route('/user/profile/setmail', method=['PUT'])
def user_profile_setmail():
    data = getData()
    token = request.form.get('token')
    email = request.form.get('email')
    #check token is valid or not
    if token_check(token) is not True:
        return dumps({
            'error' : 'invalid token'
        })
    #if the email enter is not valid
    if email_check(email) == "Invalid Email":
        raise ValueError("Invalid email address")
    #if the email address has already been used
    for key, item in data['users'].items():
        if item['email'] == email:
            raise ValueError("email address has been used")
    #decode the token and get u_id of the authorised user
    SECRET = getSecret()
    payload = jwt.decode(token, SECRET, algorithms=['HS256'])
    u_id = payload['u_id']
    #update the email
    for key, item in data['users'].items():
        if key == u_id:
            item['email'] = email
            break
    return dumps({
    })
