#from json import dumps
from flask import request, Blueprint
from data import *
from json import dumps
from uid_check import uid_check
from token_check import token_check

PROFILE = Blueprint('PROFILE', __name__)

@PROFILE.route('/user/profile', methods=['GET'])
def user_profile():
    

    u_id = int(request.args.get('u_id'))
    token = request.args.get('token')
    #print(u_id)
    #print(token)

    global data
    data = getData()

    #check token is valid or not
    if token_check(token) == False:
        print("gets in here")
        return dumps({
            'error' : 'invalid token'
        })
    #for invalid u_id given
    if uid_check(u_id) == False:
        raise ValueError("invalid u_id.")
    #get the given user's detail
    for key, item in data['users'].items():
        #print(item)
        if item['u_id'] == int(u_id):
            #print("in here")
            email = item['email']
            name_first = item['name_first']
            name_last = item['name_last']
            handle = item['handle']
            return dumps({
                'email' : email,
                'name_first' : name_first,
                'name_last' : name_last,
                'handle_str' : handle
                #'profile_img_url': None
            })
    #return
    #return dumps({
    #    'email' : email,
    #    'name_first' : name_first,
    #    'name_last' : name_last,
    #    'handle_str' : handle,
    #})
