from flask import Flask, request, Blueprint
from json import dumps
import jwt
from data import *

App = Flask(__name__)

@App.route('/user/profile', methods=['GET'])
def user_profile():
    data = getData()
    token = request.args.get('token')
    u_id = request.args.get('u_id')
    email = None
    for user in data['users']:
        if user['u_id'] == u_id:
            email= user['email']
            name_first = user['name_first']
            name_last = user['name_last']
            #handle
            break
    if email == None:
        raise ValueError('invalid u_id')
    
    return dumps({
        'email' : email
        'first_name' : first_name
        'last_name' : last_name
        'handle_str' : handle
    })
    

