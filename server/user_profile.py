from json import dumps
from flask import request, Blueprint
from data import *
from uid_check import *
from token_check import *

PROFILE = Blueprint('PROFILE', __name__)

@PROFILE.route('/user/profile', methods=['GET'])
def user_profile():
    data = getData()
    token = request.args.get('token')
    u_id = request.args.get('u_id')
    #check token is valid or not
    if token_check(token) is not True:
        return dumps({
            'error' : 'invalid token'
        })
    #for invalid u_id given
    if uid_check(u_id) is not True:
        raise ValueError("invalid u_id.")
    #get the given user's detail
    for key, item in data['users'].items():
        if key == u_id:
            email = item['email']
            name_first = item['name_first']
            name_last = item['name_last']
            handle = item['handle']
            break
    #return
    return dumps({
        'email' : email,
        'first_name' : name_first,
        'last_name' : name_last,
        'handle_str' : handle
    })
