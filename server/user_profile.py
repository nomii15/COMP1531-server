from flask import Flask, request, Blueprint
from json import dumps
from data import *
from uid_check import *

profile = Blueprint('profile', __name__)

@profile.route('/user/profile', methods=['GET'])
def user_profile():
    data = getData()
    token = request.args.get('token')
    u_id = request.args.get('u_id')
    
    #for invalid u_id given
    if uid_check(u_id) == False:
        raise ValueError("invalid u_id.")
    
    #get the given user's detail
    for key, item in data['users'].items():
        if key == u_id:
            email= item['email']
            name_first = item['name_first']
            name_last = item['name_last']
            handle = item['handle']
            break
    
    return dumps({
        'email' : email
        'first_name' : first_name
        'last_name' : last_name
        'handle_str' : handle
    })
    

