from json import dumps
from flask import request, Blueprint
import jwt
from data import *
from token_check import *

SETNAME = Blueprint('SETNAME', __name__)

@SETNAME.route('/user/profile/setname', methods=['PUT'])
def user_profile_setname():
    data = getData()
    token = request.form.get('token')
    new_name_first = str(request.form.get('name_first'))
    new_name_last = str(request.form.get('name_last'))
    #check token is valid or not
    if token_check(token) is not True:
        return dumps({
            'error' : 'invalid token'
        })
    #if name_first or name_last is not in the range of 1-50, raise exception
    if len(new_name_first) < 1 or len(new_name_first) > 50:
        raise ValueError("incorrect first name length")
    if len(new_name_last) < 1 or len(new_name_last) > 50:
        raise ValueError("incorrect last name length")
    #decode the token and get u_id of the authorised user
    SECRET = getSecret()
    payload = jwt.decode(token, SECRET, algorithms=['HS256'])
    u_id = payload['u_id']
    #update the name
    for key, item in data['users'].items():
        if key == u_id:
            item['name_first'] = new_name_first
            item['name_last'] = new_name_last
            break
    return dumps({
    })
