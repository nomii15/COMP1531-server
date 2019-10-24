from flask import Flask, request, Blueprint
from json import dumps
import jwt
from data import *

App = Flask(__name__)

@App.route('/user/profile/sethandle', method=['PUT'])
def user_profile_sethandle():
    data = getData()
    token = request.form.get('token')
    handle = request.form.get('handle_str')
    
    if len(handle)<3 or len(handle)>20:
        raise ValueError("incorrect handle length")
        
    for user in data['users']:
        if user['handle'] == handle:
            raise ValueError("handle has been used")
    
    SECRET = getSecret()
        
    Payload = jwt.decode(token, SECRET, algorithms=['HS256'])
    
    u_id = Payload['u_id']
    
    for user in data['users']:
        if user['u_id'] == u_id:
            user['handle'] = handle
