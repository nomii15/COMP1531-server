from flask import Flask, request, Blueprint
from json import dumps
import jwt
from data import *

setname = Blueprint('setname', __name__)

@setname.route('/user/profile/setname', method=['PUT'])
def user_profile_setname():
    data = getData()
    token = request.form.get('token')
    new_name_first = request.form.get('name_first')
    new_name_last = request.form.get('name_last')
    
    #if name_first or name_last is not in the range of 1-50, raise exception
    if len(new_name_first)<1 or len(new_name_first)>50:
        raise ValueError("incorrect first name length")
        
    if len(new_name_last)<1 or len(new_name_last)>50:
        raise ValueError("incorrect last name length")
    
    #decode the token and get u_id of the authorised user
    SECRET = getSecret()
    Payload = jwt.decode(token, SECRET, algorithms=['HS256'])
    u_id = Payload['u_id']
    
    #update the name
    for key, item in data['users'].items():
        if key == u_id:
            item['name_first'] = new_name_first
            item['name_last'] = new_name_last
            break
