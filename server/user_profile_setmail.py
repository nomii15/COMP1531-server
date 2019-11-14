from json import dumps
from flask import request, Blueprint
import jwt
from data import *
from email_check import email_check
from token_check import token_check

SETMAIL = Blueprint('SETMAIL', __name__)

def user_profile_setmail(token, email):
    data = getData()    
    #check token is valid or not
    if token_check(token) is not True:
        return {
            'error' : 'invalid token'
        }
    #if the email enter is not valid
    if email_check(email) == "Invalid Email":
        raise ValueError(description = "Invalid email address")
    #if the email address has already been used
    for key, item in data['users'].items():
        if item['email'] == email:
            raise ValueError(description = "email address has been used")            
    #decode the token and get u_id of the authorised user
    SECRET = getSecret()
    payload = jwt.decode(token, SECRET, algorithms=['HS256'])
    u_id = payload['u_id']
    #update the email
    for key, item in data['users'].items():
        if key == u_id:
            item['email'] = email
            break
    return {
    }

@SETMAIL.route('/user/profile/setemail', methods=['PUT'])    
def user_profile_setmail_route():
    token = request.form.get('token')
    email = request.form.get('email')
    return dumps(user_profile_setmail(token, email))
