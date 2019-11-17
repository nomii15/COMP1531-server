from json import dumps
from flask import request, Blueprint
import jwt
from token_to_uid import token_to_uid
from data import *
from token_check import token_check

SETNAME = Blueprint('SETNAME', __name__)

def user_profile_setname(token, name_first, name_last):
    data = getData()
    #check token is valid or not
    if token_check(token) is not True:
        return {
            'error' : 'invalid token'
        }
    #if name_first or name_last is not in the range of 1-50, raise exception
    if len(name_first) < 1 or len(name_first) > 50:
        raise ValueError(description = "incorrect first name length")
    if len(name_last) < 1 or len(name_last) > 50:
        raise ValueError(description = "incorrect last name length")
    #decode the token and get u_id of the authorised user
    u_id = token_to_uid(token)
    #update the name
    for key, item in data['users'].items():
        if key == u_id:
            item['name_first'] = name_first
            item['name_last'] = name_last
            break
    return {
    }

@SETNAME.route('/user/profile/setname', methods=['PUT'])   
def user_profile_setname_route():
    token = request.form.get('token')
    name_first = str(request.form.get('name_first'))
    name_last = str(request.form.get('name_last'))
    return dumps(user_profile_setname(token, name_first, name_last))
