from flask import Flask, request, Blueprint
from json import dumps
import jwt
from data import *

App = Flask(__name__)

@App.route('/user/profile/setname', method=['PUT'])
def user_profile_setname():
    data = getData()
    token = request.form.get('token')
    new_name_first = request.form.get('name_first')
    new_name_last = request.form.get('name_last')
    
    if len(new_name_first)<1 or len(new_name_first)>50:
        raise ValueError("incorrect first name length")
        
    if len(new_name_last)<1 or len(new_name_last)>50:
        raise ValueError("incorrect last name length")
    
    SECRET = getSecret()
        
    Payload = jwt.decode(token, SECRET, algorithms=['HS256'])
    
    u_id = Payload['u_id']
    
    for user in data['users']:
        if user['u_id'] == u_id:
            user['name_first'] = new_name_first
            user['name_last'] = new_name_last
