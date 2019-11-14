from json import dumps
from flask import request, Blueprint
import jwt
from token_check import token_check
from data import *


SETHANDLE = Blueprint('SETHANDLE', __name__)

def user_profile_sethandle(token, handle):
    data = getData()    
    #check token is valid or not
    if token_check(token) is not True:
        return {
            'error' : 'invalid token'
        }
    #the handle must in the range of 3-20
    if len(handle) < 3 or len(handle) > 20:
        raise ValueError(description = "incorrect handle length")
    #if the handle is already been used, raise exception
    for key, item in data['users'].items():
        if item['handle'] == handle:
            raise ValueError(description = "handle has been used")
    #decode the token and get u_id of the authorised user
    SECRET = getSecret()
    payload = jwt.decode(token, SECRET, algorithms=['HS256'])
    u_id = payload['u_id']
    #update the handle
    for key, item in data['users'].items():
        if key == u_id:
            item['handle'] = handle
            break
    return {
    }
    
@SETHANDLE.route('/user/profile/sethandle', methods=['PUT'])
def user_profile_sethandle_route():
    token = request.form.get('token')
    handle = str(request.form.get('handle_str'))
    return dumps(user_profile_sethandle(token, handle))
