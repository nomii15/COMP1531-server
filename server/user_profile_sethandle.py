from flask import Flask, request, Blueprint
from json import dumps
import jwt
from data import *

sethandle = Blueprint('sethandle', __name__)

@sethandle.route('/user/profile/sethandle', method=['PUT'])
def user_profile_sethandle():
    data = getData()
    token = request.form.get('token')
    handle = request.form.get('handle_str')
    
    #the handle must in the range of 3-20
    if len(handle)<3 or len(handle)>20:
        raise ValueError("incorrect handle length")
        
    #if the handle is already been used, raise exception    
    for key, item in data['users'].items():
        if item['handle'] == handle:
            raise ValueError("handle has been used")
    
    #decode the token and get u_id of the authorised user 
    SECRET = getSecret()
    Payload = jwt.decode(token, SECRET, algorithms=['HS256'])
    u_id = Payload['u_id']
    
    #update the handle
    for key, item in data['users'].items():
        if key == u_id:
            item['handle'] = handle
            break
